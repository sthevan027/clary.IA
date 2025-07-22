# Passo a Passo - Clary.AI

## 1. Pré-requisitos
- Python 3.10+
- Conta no Discord Developer Portal
- (Opcional) Conta no Notion e database criada
- (Opcional) Conta no GitHub com permissão para configurar webhooks
- (Opcional) Docker instalado

---

## 2. Instalação do Projeto

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd clary.IA
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   pip install notion-client flask
   ```

---

## 3. Configuração do .env
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
DISCORD_TOKEN=seu_token_do_bot
CHANNEL_ID=id_do_canal_do_discord
NOTION_TOKEN=seu_token_notion (opcional)
NOTION_DATABASE_ID=seu_database_id_notion (opcional)
```

---

## 4. Executando o Bot

```bash
python src/bot.py
```

---

## 5. Integração com Notion (opcional)
1. Crie uma integração no Notion e copie o token de integração.
2. Compartilhe sua database com a integração criada.
3. Pegue o ID da database (está na URL ao abrir a database).
4. Preencha `NOTION_TOKEN` e `NOTION_DATABASE_ID` no `.env`.
5. O bot já está pronto para salvar resumos no Notion (verifique o serviço em `src/services/notion.py`).

---

## 6. Integração com GitHub (opcional)
1. Instale o Flask: `pip install flask`
2. Rode o serviço Flask:
   ```bash
   python src/services/github_webhook.py
   ```
3. No GitHub, vá em Settings > Webhooks do seu repositório.
4. Adicione um webhook apontando para:
   ```
   http://<seu-servidor>:5000/github-webhook
   ```
5. Selecione os eventos desejados (Pull requests, Deployments, etc).
6. Personalize as mensagens de alerta em `config/alerts.json`.

---

## 7. Subindo o projeto com Docker (opcional)

1. Crie um arquivo `Dockerfile` na raiz do projeto com o seguinte conteúdo:
   ```dockerfile
   FROM python:3.10-slim
   WORKDIR /app
   COPY . .
   RUN pip install --no-cache-dir -r requirements.txt && \
       pip install notion-client flask
   CMD ["python", "src/bot.py"]
   ```
2. Crie a imagem Docker:
   ```bash
   docker build -t claryai .
   ```
3. Execute o container, garantindo que o `.env` está presente:
   ```bash
   docker run --env-file .env claryai
   ```

---

## 8. Comandos Principais
- Veja a lista completa de comandos e exemplos no README.md

---

## 9. Dúvidas ou Problemas?
Abra uma issue no repositório ou entre em contato com o mantenedor. 