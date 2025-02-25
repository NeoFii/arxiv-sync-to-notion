# config.py

# Notion API 密钥（在 GitHub Actions 中通过环境变量设置）
NOTION_API_KEY = 'your_notion_api_key'

# Notion 数据库 ID（在 GitHub Actions 中通过环境变量设置）
NOTION_DATABASE_ID = 'your_database_id'

# Arxiv 类别和最大结果数
ARXIV_CATEGORIES = ['cs.AI', 'cs.LG']  # 可根据需要修改类别
MAX_RESULTS = 10  # 每次获取的论文数量