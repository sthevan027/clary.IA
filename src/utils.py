import os
from datetime import datetime

CEO_ROLES = ['ceo', 'líder técnico']

# Checa se o usuário tem permissão de CEO/líder técnico
def is_ceo(member):
    return any(role.name.lower() in CEO_ROLES for role in member.roles)

# Loga comandos em logs/YYYY-MM-DD.log
def log_command(ctx, comando, extra=None):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    data_log = datetime.now().strftime('%Y-%m-%d')
    hora = datetime.now().strftime('%H:%M:%S')
    usuario = f'{ctx.author.display_name}#{ctx.author.discriminator} (ID: {ctx.author.id})'
    canal = ctx.channel.name if hasattr(ctx.channel, 'name') else str(ctx.channel)
    msg = f'{hora} | {comando} | {usuario} | {canal}'
    if extra:
        msg += f' | {extra}'
    with open(f'logs/{data_log}.log', 'a', encoding='utf-8') as f:
        f.write(msg + '\n') 