"""
Defines the configurations for the celery
task. 'result_backend' define the db to
send worker's results, 'broker_url' defines
main db, 'app.autodiscover_tasks' imports
all that is in the project directory, and
'timezone' defines timezone for use in beat.
"""
from app import app


result_backend = "redis://localhost:6379/0"
broker_url = "redis://localhost:6379/0"
app.autodiscover_tasks(packages=["celery"])
timezone = "Europe/Lisbon"
