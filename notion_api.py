# notion_api.py

from notion_client import Client
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_to_notion(papers, notion_api_key, database_id):
    """将论文添加到 Notion 数据库"""
    notion = Client(auth=notion_api_key)
    existing_papers = {}
    
    try:
        results = notion.databases.query(database_id=database_id)
        for page in results.get('results', []):
            properties = page.get('properties', {})
            title_property = properties.get('Title', {})
            title = title_property.get('title', [{}])[0].get('text', {}).get('content', '') if title_property.get('title') else ''
            existing_papers[title] = True
        logging.info(f"找到 {len(existing_papers)} 篇现有论文")
    except Exception as e:
        logging.error(f"获取现有论文时出错: {e}")
        return 0
    
    added_count = 0
    for paper in papers:
        if paper['title'] in existing_papers:
            logging.info(f"跳过已有论文: {paper['title']}")
            continue
        try:
            new_page = {
                "parent": {"database_id": database_id},
                "properties": {
                    "Title": {"title": [{"text": {"content": paper['title']}}]},
                    "Authors": {"rich_text": [{"text": {"content": ", ".join(paper['authors'])}}]},
                    "Published Date": {"date": {"start": paper['published']}},
                    "Categories": {"multi_select": [{"name": cat} for cat in paper['categories']]},
                    "Primary Category": {"select": {"name": paper['primary_category']}},
                    "URL": {"url": paper['link']},
                    "PDF": {"url": paper['pdf_link']}
                },
                "children": [
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{"type": "text", "text": {"content": paper['summary']}}]
                        }
                    }
                ]
            }
            notion.pages.create(**new_page)
            added_count += 1
            logging.info(f"成功添加论文: {paper['title']}")
        except Exception as e:
            logging.error(f"添加论文 '{paper['title']}' 到 Notion 时出错: {e}")
    return added_count