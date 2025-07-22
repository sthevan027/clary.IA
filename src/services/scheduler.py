from apscheduler.schedulers.asyncio import AsyncIOScheduler

def start_scheduler(bot):
    scheduler = AsyncIOScheduler()
    # Exemplo de tarefa agendada:
    # scheduler.add_job(lambda: print('Tarefa agendada!'), 'cron', hour=21, minute=0)
    scheduler.start() 