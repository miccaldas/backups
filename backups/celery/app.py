"""
Instantiates a Celery object, defines celery
schedule as being in the rontab format,
define the
backend for worker information, database,
tells it to include the main.py file
as the module to launch, when called,
and defines a periodic task to be included
on beat.
"""

from celery import Celery
from celery.schedules import crontab

app = Celery(
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
    include=["main"],
    beat_schedule={
        "backup_cron": {"task": "tasks.go", "schedule": crontab(minute=0, hour=16)},
    },
)

if __name__ == "__main__":
    app()
