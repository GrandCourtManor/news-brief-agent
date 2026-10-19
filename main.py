import os
import feedparser
import requests
from dotenv import load_dotenv
from openai import OpenAI
from config import RSS_FEEDS, SYSTEM_PROMPT
from utils import save_brief

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)
MODEL = os.getenv("DEEPSEEK_MODEL")
LIMIT = int(os.getenv("NEWS_LIMIT", 8))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_rss_news():
    news_items = []
    for feed in RSS_FEEDS:
        print(f"🔍 正在抓取: {feed['name']} url={feed['url']}")
        try:
            resp = requests.get(feed["url"], headers=HEADERS, timeout=10)
            resp.raise_for_status()
            d = feedparser.parse(resp.content)
            print(f"✅ {feed['name']} 抓到 {len(d.entries)} 条")
            for entry in d.entries[:LIMIT]:
                item = {
                    "source": feed["name"],
                    "title": entry.get("title", ""),
                    "summary": entry.get("summary", ""),
                    "link": entry.get("link", "")
                }
                news_items.append(item)
        except Exception as e:
            print(f"⚠️ {feed['name']} 抓取失败：{type(e).__name__}: {e}")
    return news_items

def build_user_prompt(news_list):
    text = "下面是今天抓取到的新闻列表：\n\n"
    for n in news_list:
        text += f"【{n['source']}】{n['title']}\n摘要：{n['summary']}\n链接：{n['link']}\n---\n"
    text += "\n请按照要求生成新闻简报"
    return text

def generate_brief(news_list):
    resp = client.chat.completions.create(
        model=MODEL,
        max_tokens=1500,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(news_list)}
        ]
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    news = fetch_rss_news()
    print(f"\n📰 一共汇总到新闻条数：{len(news)}")
    if not news:
        print("❌ 没有抓到新闻")
        exit()
    brief_md = generate_brief(news)
    save_brief(brief_md)
    print("\n===== 生成简报完成 =====")
    print(brief_md)
