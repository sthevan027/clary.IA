from discord.ext import commands
from datetime import datetime, timedelta
from src.services.alerts import load_alerts
from src.utils import log_command
import asyncio

# Função para converter HH:MM para segundos até o horário
def segundos_ate_horario(horario):
    agora = datetime.now()
    alvo = datetime.strptime(horario, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
    if alvo < agora:
        alvo += timedelta(days=1)
    return (alvo - agora).total_seconds()

def setup(bot):
    @bot.command(name='lembrete')
    async def lembrete(ctx, horario: str, *, mensagem: str):
        log_command(ctx, '!lembrete', f'{horario} {mensagem}')
        try:
            segundos = segundos_ate_horario(horario)
            await ctx.send(f'Lembrete agendado para {horario}!')
            await asyncio.sleep(segundos)
            alerts = load_alerts()
            texto = alerts.get('lembrete', '⏰ Lembrete: {mensagem}').replace('{mensagem}', mensagem)
            await ctx.send(f'{ctx.author.mention} {texto}')
        except Exception as e:
            await ctx.send(f'Erro ao agendar lembrete: {e}') 