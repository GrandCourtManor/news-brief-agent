import os
import re
from datetime import datetime
from openpyxl import Workbook

def get_today_str():
    return datetime.now().strftime("%Y-%m-%d")

def save_brief(content: str):
    os.makedirs("briefs", exist_ok=True)
    day = get_today_str()
    path = f"briefs/news-brief-{day}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Markdown简报已保存到 {path}")
    return path

def clean_html(raw_text: str) -> str:
    """清理RSS摘要里的HTML标签和多余空白，只保留纯文本"""
    if not raw_text:
        return ""
    text = re.sub(r'<[^>]+>', '', raw_text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def save_news_to_excel(news_list: list):
    """把原始新闻明细保存为Excel表格"""
    os.makedirs("briefs", exist_ok=True)
    day_str = get_today_str()
    file_path = f"briefs/news-{day_str}.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = "今日新闻"

    # 表头
    headers = ["序号", "来源", "标题", "摘要", "原文链接", "抓取时间"]
    ws.append(headers)

    # 写入数据
    for idx, item in enumerate(news_list, 1):
        ws.append([
            idx,
            item.get("source", ""),
            item.get("title", ""),
            clean_html(item.get("summary", "")),
            item.get("link", ""),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

    # 调整列宽
    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 12
    ws.column_dimensions['C'].width = 50
    ws.column_dimensions['D'].width = 80
    ws.column_dimensions['E'].width = 50
    ws.column_dimensions['F'].width = 20

    wb.save(file_path)
    print(f"📊 Excel新闻表格已保存到 {file_path}")
    return file_path
