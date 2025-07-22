from discord.ext import commands
from datetime import datetime
from src.utils import log_command
import os

RESUMOS_PATH = 'resumos'

def setup(bot):
    @bot.command(name='resumo')
    async def resumo(ctx, data: str = None):
        data_ref = data if data else datetime.now().strftime('%Y-%m-%d')
        caminho = f'{RESUMOS_PATH}/{data_ref}.txt'
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            await ctx.send(f'Resumo de {data_ref}:\n{conteudo[:1900]}')
        else:
            await ctx.send(f'Nenhum resumo encontrado para {data_ref}.')
        log_command(ctx, '!resumo', data_ref) 