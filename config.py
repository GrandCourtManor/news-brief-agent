# 稳定可用原生RSS源
RSS_FEEDS = [
    {"name": "IT之家", "url": "https://www.ithome.com/rss/"},
    {"name": "爱范儿", "url": "https://www.ifanr.com/feed"},
    {"name": "第一财经", "url": "https://www.yicai.com/feed"},
    {"name": "Solidot科技", "url": "https://www.solidot.org/index.rss"},
]

# 核心Prompt，发给大模型，控制简报格式
SYSTEM_PROMPT = """
你是专业新闻简报助手，基于给到的新闻条目生成【每日新闻早报】
要求：
1. 先一句话总述今天重点趋势
2. 分点整理，每条新闻：【来源标题】+ 核心摘要（精简，不要废话）
3. 最后增加一个板块：📌 值得关注
4. 输出严格使用markdown，不要多余闲聊，不要幻觉编造内容
5. 如果新闻内容不足，如实说明
"""
