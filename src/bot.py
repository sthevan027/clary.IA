import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from .commands import register_commands
from .services.scheduler import start_scheduler

# Carrega as variáveis de ambiente
load_dotenv()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')
    start_scheduler(bot)

register_commands(bot)

# Verifica se o token existe
token = os.getenv('DISCORD_TOKEN')
if not token:
    raise ValueError("Token do Discord não encontrado no arquivo .env")

bot.run(token) 