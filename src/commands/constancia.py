from discord.ext import commands
from datetime import datetime, timedelta
from src.utils import log_command
import os

RESUMOS_PATH = 'resumos'

def setup(bot):
    @bot.command(name='constancia')
    async def constancia(ctx):
        hoje = datetime.now()
        dias_c = 0
        total = 0
        for i in range(7):
            data = (hoje - timedelta(days=i)).strftime('%Y-%m-%d')
            caminho = f'{RESUMOS_PATH}/{data}.txt'
            if os.path.exists(caminho):
                with open(caminho, 'r', encoding='utf-8') as f:
                    entregas = [l for l in f if ctx.author.display_name in l]
                    if entregas:
                        dias_c += 1
                        total += len(entregas)
        await ctx.send(f'Você codou {dias_c} dias e entregou {total} itens na última semana.')
        log_command(ctx, '!constancia') 