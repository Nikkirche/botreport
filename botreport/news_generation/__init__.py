from apscheduler.schedulers.background import BackgroundScheduler


def generate():
    from .generate.parse import Controller
    test = Controller()
    match = test[1]
    match.update()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate, 'interval', seconds=60)
    scheduler.start()


try:
    start()
    pass
except:
    pass
