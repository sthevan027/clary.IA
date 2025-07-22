from discord.ext import commands
from src.utils import log_command
import os

TEMPLATE_PATH = 'resumos/template.txt'

def setup(bot):
    @bot.command(name='settemplate')
    async def settemplate(ctx, *, template: str):
        if not os.path.exists('resumos'):
            os.makedirs('resumos')
        with open(TEMPLATE_PATH, 'w', encoding='utf-8') as f:
            f.write(template)
        log_command(ctx, '!settemplate', template)
        await ctx.send('Template atualizado!') 