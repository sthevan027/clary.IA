from flask import Flask, request
import os
import discord
import asyncio
from src.services.alerts import load_alerts

app = Flask(__name__)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))

loop = asyncio.get_event_loop()

client = discord.Client(intents=discord.Intents.default())

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    data = request.json
    alerts = load_alerts()
    if data.get('action') == 'closed' and data.get('pull_request', {}).get('merged'):
        user = data['pull_request']['merged_by']['login']
        msg = alerts.get('pr_merged', '🟢 PR mergeado por {user}').replace('{user}', user)
        loop.create_task(enviar_alerta(msg))
    if data.get('deployment_status', {}).get('state') == 'success':
        msg = alerts.get('deploy', '🚀 Novo deploy realizado!')
        loop.create_task(enviar_alerta(msg))
    return '', 200

async def enviar_alerta(msg):
    await client.wait_until_ready()
    canal = client.get_channel(CHANNEL_ID)
    if canal:
        await canal.send(msg)

# Para rodar: flask run ou python src/services/github_webhook.py
if __name__ == '__main__':
    client.loop.create_task(app.run(port=5000))
    client.run(DISCORD_TOKEN) 