from discord.ext import commands
from datetime import datetime
from src.utils import log_command

TEMAS = {
    0: 'Python avançado',
    1: 'APIs e Integrações',
    2: 'Banco de Dados',
    3: 'Clean Code e boas práticas',
    4: 'Testes automatizados',
    5: 'DevOps e Deploy',
    6: 'Projetos Open Source'
}

def setup(bot):
    @bot.command(name='estudo')
    async def estudo(ctx):
        dia = datetime.now().weekday()
        tema = TEMAS.get(dia, 'Tema livre')
        await ctx.send(f'Sugestão de estudo para hoje: {tema}')
        log_command(ctx, '!estudo', tema) 