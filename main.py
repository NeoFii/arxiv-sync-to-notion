# main.py

import os
from config import NOTION_API_KEY, NOTION_DATABASE_ID, ARXIV_CATEGORIES, MAX_RESULTS
from arxiv_api import get_arxiv_papers
from notion_api import add_to_notion
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    # 从环境变量中获取敏感信息（如果设置）
    NOTION_API_KEY = os.getenv('NOTION_API_KEY', NOTION_API_KEY)
    NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID', NOTION_DATABASE_ID)
    
    papers = get_arxiv_papers(ARXIV_CATEGORIES, MAX_RESULTS)
    added_count = add_to_notion(papers, NOTION_API_KEY, NOTION_DATABASE_ID)
    logging.info(f"成功添加 {added_count} 篇新论文到 Notion")