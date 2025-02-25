# arxiv_api.py

import requests
import xml.etree.ElementTree as ET
import datetime
import urllib.parse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_arxiv_papers(categories, max_results):
    """从 Arxiv 获取指定领域的最新论文"""
    papers = []
    for category in categories:
        query = f'cat:{category}'
        encoded_query = urllib.parse.quote(query)
        url = f'http://export.arxiv.org/api/query?search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            logging.info(f"成功获取 {category} 类别的论文")
        except requests.exceptions.RequestException as e:
            logging.error(f"获取 {category} 类别的论文失败: {e}")
            continue
        
        root = ET.fromstring(response.content)
        namespace = {'atom': 'http://www.w3.org/2005/Atom'}
        
        for entry in root.findall('.//atom:entry', namespace):
            title = entry.find('./atom:title', namespace).text.strip()
            summary = entry.find('./atom:summary', namespace).text.strip()
            published = entry.find('./atom:published', namespace).text
            published_date = datetime.datetime.strptime(published, '%Y-%m-%dT%H:%M:%SZ')
            authors = [author.text for author in entry.findall('./atom:author/atom:name', namespace)]
            link = entry.find('./atom:id', namespace).text
            pdf_link = link.replace('abs', 'pdf')
            categories_list = [cat.get('term') for cat in entry.findall('./atom:category', namespace) if cat.get('term')]
            
            paper = {
                'title': title,
                'summary': summary,
                'authors': authors,
                'published': published_date.strftime('%Y-%m-%d'),
                'link': link,
                'pdf_link': pdf_link,
                'categories': categories_list,
                'primary_category': category
            }
            papers.append(paper)
    return papers