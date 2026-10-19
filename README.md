# Claude News Brief Agent
> 基于 Claude API + RSS 自动抓取新闻，生成每日Markdown新闻简报。

## ✨ Features
- 自动抓取RSS新闻源
- 调用Claude 3 智能摘要、整理结构化简报
- 自动保存为日期命名的 Markdown 文件
- 可扩展：飞书推送、定时任务、多数据源

## 📦 Install
```bash
git clone https://github.com/你的用户名/news-brief-agent.git
cd news-brief-agent
python -m venv .venv
pip install -r requirements.txt
# news-brief-agent
本项目是轻量化 LLM Agent，实现资讯自动化采集与摘要生成。程序拉取 RSS 新闻源后，调用 Claude 对多条资讯做去冗余、要点提炼、趋势总结，输出标准化 Markdown 简报。支持本地手动运行 + GitHub Actions 定时调度，新增推送接口即可对接飞书、邮件等渠道，适合搭建个人每日资讯订阅工具。
