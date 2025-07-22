import os
from notion_client import Client
from datetime import datetime

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

notion = Client(auth=NOTION_TOKEN) if NOTION_TOKEN else None

def salvar_resumo_notion(conteudo, data=None):
    if not notion:
        return False, 'Notion não configurado.'
    data = data or datetime.now().strftime('%Y-%m-%d')
    try:
        notion.pages.create(
            parent={"database_id": NOTION_DATABASE_ID},
            properties={
                "Name": {"title": [{"text": {"content": f"Resumo {data}"}}]},
                "Data": {"date": {"start": data}},
            },
            children=[{"object": "block", "type": "paragraph", "paragraph": {"text": [{"type": "text", "text": {"content": conteudo}}]}}]
        )
        return True, 'Resumo salvo no Notion!'
    except Exception as e:
        return False, f'Erro ao salvar no Notion: {e}' 