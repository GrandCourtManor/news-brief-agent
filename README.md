# news-brief-agent
本项目是轻量化 LLM Agent，实现资讯自动化采集与摘要生成。程序拉取 RSS 新闻源后，调用 Claude 对多条资讯做去冗余、要点提炼、趋势总结，输出标准化 Markdown 简报。支持本地手动运行 + GitHub Actions 定时调度，新增推送接口即可对接飞书、邮件等渠道，适合搭建个人每日资讯订阅工具。
