# Clary.AI - Bot Discord para Produtividade

Bot Discord para automatizar mensagens, resumos, insights e alertas para times técnicos.

## Funcionalidades

- Comandos de produtividade para equipes técnicas
- Resumo diário automático às 21h
- Adição e consulta de resumos, progresso, ideias e constância
- Lembretes personalizados
- Sugestão de estudo do dia
- Logs de atividades do bot
- Customização de templates e alertas
- Integração com Notion (salvar resumos)
- Integração com GitHub (alertas de PR/deploy via webhook)

## Requisitos

- Python 3.10+
- Conta no Discord Developer Portal
- Token do bot Discord
- (Opcional) Token e Database ID do Notion
- (Opcional) Flask para webhooks do GitHub

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
pip install notion-client flask
```

3. Configure o arquivo `.env`:
```
DISCORD_TOKEN=seu_token_aqui
CHANNEL_ID=id_do_canal_aqui
NOTION_TOKEN=seu_token_notion
NOTION_DATABASE_ID=seu_database_id_notion
```

## Executando o Bot

```bash
python src/bot.py
```

## Comandos Disponíveis

- `!ping` - Testa se o bot está online
- `!addresumo <mensagem>` - Adiciona uma informação ao resumo do dia
- `!resumo [AAAA-MM-DD]` - Mostra o resumo do dia (ou de uma data)
- `!progresso` - Mostra suas entregas do dia
- `!ideia <mensagem>` - Salva uma ideia técnica
- `!estudo` - Sugere tema de estudo do dia
- `!constancia` - Mostra sua constância semanal
- `!resumo_semana` - Mostra resumo dos últimos 7 dias
- `!resumo_mes` - Mostra resumo dos últimos 30 dias
- `!settemplate <template>` - Define o template do resumo diário
- `!exportar` - Exporta todos os resumos do mês em um arquivo
- `!lembrete HH:MM mensagem` - Agenda um lembrete personalizado

## Integração com Notion
- Os resumos podem ser salvos automaticamente em uma database do Notion.
- Configure `NOTION_TOKEN` e `NOTION_DATABASE_ID` no `.env`.

## Integração com GitHub
- Receba alertas de PRs e deploys via webhook.
- Configure o webhook do GitHub para `http://<seu-servidor>:5000/github-webhook`.
- Personalize as mensagens de alerta em `config/alerts.json`.

---

Para dúvidas ou sugestões, abra uma issue ou entre em contato!