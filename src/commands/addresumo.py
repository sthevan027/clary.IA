from discord.ext import commands
from datetime import datetime
from src.utils import log_command
import os

RESUMOS_PATH = 'resumos'

# Garante que a pasta existe
def garantir_pasta():
    if not os.path.exists(RESUMOS_PATH):
        os.makedirs(RESUMOS_PATH)

def setup(bot):
    @bot.command(name='addresumo')
    async def addresumo(ctx, *, mensagem: str):
        garantir_pasta()
        data_hoje = datetime.now().strftime('%Y-%m-%d')
        caminho = f'{RESUMOS_PATH}/{data_hoje}.txt'
        autor = ctx.author.display_name
        with open(caminho, 'a', encoding='utf-8') as f:
            f.write(f'- {mensagem} (por {autor})\n')
        log_command(ctx, '!addresumo', mensagem)
        await ctx.send('Resumo registrado!') 