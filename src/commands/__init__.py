def register_commands(bot):
    from .ping import setup as setup_ping
    setup_ping(bot)
    from .lembrete import setup as setup_lembrete
    setup_lembrete(bot)
    from .addresumo import setup as setup_addresumo
    setup_addresumo(bot)
    from .resumo import setup as setup_resumo
    setup_resumo(bot)
    from .progresso import setup as setup_progresso
    setup_progresso(bot)
    from .ideia import setup as setup_ideia
    setup_ideia(bot)
    from .estudo import setup as setup_estudo
    setup_estudo(bot)
    from .constancia import setup as setup_constancia
    setup_constancia(bot)
    from .resumo_semana import setup as setup_resumo_semana
    setup_resumo_semana(bot)
    from .resumo_mes import setup as setup_resumo_mes
    setup_resumo_mes(bot)
    from .settemplate import setup as setup_settemplate
    setup_settemplate(bot)
    from .exportar import setup as setup_exportar
    setup_exportar(bot)
    # Adicione aqui os setups dos outros comandos 