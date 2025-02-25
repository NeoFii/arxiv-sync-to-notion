# Arxiv Sync to Notion (v0.0.1)

This project automatically syncs the latest papers from Arxiv to a Notion database.

## Features
- Fetches papers from specified Arxiv categories.
- Adds new papers to a Notion database, avoiding duplicates.
- Runs automatically daily via GitHub Actions.

## Setup
1. Clone the repository: `git clone https://github.com/NeoFii/arxiv-sync-to-notion.git`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up Notion API and database:
   - Create a Notion integration and obtain the API key.
   - Create a database and note its ID.
4. Configure `config.py` or use environment variables for sensitive information.

## Usage
Run `python main.py` to sync papers manually.

## GitHub Actions
- The workflow runs daily at UTC 00:00.
- Manual triggers are available through the GitHub Actions tab.
- Add `NOTION_API_KEY` and `NOTION_DATABASE_ID` to repository secrets.

## License
MIT License