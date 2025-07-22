from discord.ext import commands
from datetime import datetime
from src.utils import log_command
import os

IDEIAS_PATH = 'ideias'

def garantir_pasta():
    if not os.path.exists(IDEIAS_PATH):
        os.makedirs(IDEIAS_PATH)

def setup(bot):
    @bot.command(name='ideia')
    async def ideia(ctx, *, mensagem: str):
        garantir_pasta()
        data_hoje = datetime.now().strftime('%Y-%m-%d')
        caminho = f'{IDEIAS_PATH}/{data_hoje}.txt'
        autor = ctx.author.display_name
        with open(caminho, 'a', encoding='utf-8') as f:
            f.write(f'- {mensagem} (por {autor})\n')
        log_command(ctx, '!ideia', mensagem)
        await ctx.send('Ideia registrada!') 