from discord.ext import commands
from datetime import datetime, timedelta
from src.utils import log_command
import os
from discord import File

RESUMOS_PATH = 'resumos'

def setup(bot):
    @bot.command(name='exportar')
    async def exportar(ctx):
        hoje = datetime.now()
        export_path = f'{RESUMOS_PATH}/export_{hoje.strftime("%Y-%m")}.txt'
        with open(export_path, 'w', encoding='utf-8') as out:
            for i in range(30):
                data = (hoje - timedelta(days=i)).strftime('%Y-%m-%d')
                caminho = f'{RESUMOS_PATH}/{data}.txt'
                if os.path.exists(caminho):
                    with open(caminho, 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                    out.write(f'--- {data} ---\n{conteudo}\n')
        await ctx.send(file=File(export_path))
        log_command(ctx, '!exportar') 