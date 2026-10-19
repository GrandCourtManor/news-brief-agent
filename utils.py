from datetime import datetime
import os

def get_today_str():
    return datetime.now().strftime("%Y-%m-%d")

def save_brief(content: str):
    os.makedirs("briefs", exist_ok=True)
    day = get_today_str()
    path = f"briefs/news-brief-{day}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 简报已保存到 {path}")
    return path
