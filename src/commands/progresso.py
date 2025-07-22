from discord.ext import commands
from datetime import datetime
from src.utils import log_command
import os

RESUMOS_PATH = 'resumos'

def setup(bot):
    @bot.command(name='progresso')
    async def progresso(ctx):
        data_hoje = datetime.now().strftime('%Y-%m-%d')
        caminho = f'{RESUMOS_PATH}/{data_hoje}.txt'
        entregas = []
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as f:
                for linha in f:
                    if ctx.author.display_name in linha:
                        entregas.append(linha.strip())
        if entregas:
            await ctx.send(f'Suas entregas de hoje:\n' + '\n'.join(entregas))
        else:
            await ctx.send('Nenhuma entrega registrada por você hoje.')
        log_command(ctx, '!progresso') 