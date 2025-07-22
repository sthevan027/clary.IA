from discord.ext import commands
from datetime import datetime, timedelta
from src.utils import log_command
import os

RESUMOS_PATH = 'resumos'

def setup(bot):
    @bot.command(name='resumo_mes')
    async def resumo_mes(ctx):
        hoje = datetime.now()
        resumos = []
        for i in range(30):
            data = (hoje - timedelta(days=i)).strftime('%Y-%m-%d')
            caminho = f'{RESUMOS_PATH}/{data}.txt'
            if os.path.exists(caminho):
                with open(caminho, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                resumos.append(f'--- {data} ---\n{conteudo}')
        if resumos:
            await ctx.send('\n\n'.join(resumos)[:1900])
        else:
            await ctx.send('Nenhum resumo encontrado para os últimos 30 dias.')
        log_command(ctx, '!resumo_mes') 