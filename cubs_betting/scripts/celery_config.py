from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.beat_schedule = {
    'fetch-odds-every-5-minutes': {
        'task': 'tasks.fetch_odds_data',
        'schedule': 300.0,  # 5 minutes
    },
}
app.conf.timezone = 'UTC'
