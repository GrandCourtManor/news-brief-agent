# News Brief Agent
基于 RSS + DeepSeek API 自动抓取资讯，生成每日结构化新闻简报，并导出原始新闻明细 Excel。

## 📖 项目简介
本项目是轻量化 LLM 资讯采集 Agent，定时拉取多个 RSS 新闻源，自动清洗网页 HTML 摘要，调用大模型提炼重点、整合趋势，输出规范 Markdown 简报，同时导出带来源、标题、链接的 Excel 原始新闻表。支持 GitHub Actions 定时自动运行，每天自动产出早报。

## 🧩 背景与问题
日常需要持续关注科技、财经资讯，但分散在多个网站：
- 逐个打开网站浏览耗时，信息碎片化；
- 新闻内容混杂 HTML 标签、广告、冗余文本，阅读效率低；
- 难以快速提炼当日行业趋势、重点事件；
- 想要留存原始新闻清单，方便后续复盘、检索。

本项目通过 RSS 统一聚合 + LLM 摘要，一键完成采集、清洗、总结、归档。

## ✨ 核心能力
- ✅ 多源 RSS 自动抓取：IT之家、36氪、虎嗅、界面新闻、Solidot、爱范儿等稳定资讯源
- ✅ 文本自动清洗：自动剔除 RSS 摘要内 HTML 标签、多余空白
- ✅ AI 智能摘要：调用 DeepSeek 对新闻去重提炼，生成结构化 Markdown 简报，包含趋势总览、分条要点、值得关注板块
- ✅ 双文件归档：
  - Markdown：整理后的精简新闻早报，适合直接阅读
  - Excel：原始新闻明细（序号 / 来源 / 标题 / 摘要 / 链接 / 抓取时间），用于存档筛选
- ✅ 定时自动化：接入 GitHub Actions，配置 UTC cron 定时任务，每日自动运行
- ✅ 易于扩展：新增 RSS 源仅需修改配置文件；可继续接入飞书/企业微信推送

## 🛠️ 技术架构
- 采集层：`requests` 请求 RSS 源 + `feedparser` 解析 XML
- 清洗层：正则表达式去除 HTML 标签，规整文本
- LLM 层：兼容 OpenAI 协议，调用 DeepSeek API 做内容总结
- 存储层：`openpyxl` 生成 Excel；原生文件写入 Markdown
- 调度层：GitHub Actions（定时 cron + 手动触发）
- 配置管理：`python-dotenv` 管理密钥，`.gitignore` 保护隐私，不上传 API Key 和生成产物

## 📦 Install
```bash
git clone https://github.com/GrandCourtManor/news-brief-agent.git
cd news-brief-agent
python -m venv .venv
pip install -r requirements.txt

