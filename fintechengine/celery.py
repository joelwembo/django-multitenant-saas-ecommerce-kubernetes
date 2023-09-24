from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fintechengine.settings")

app = Celery("fintechengine")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
# # Executes every Monday morning at 7:30 a.m.
# # 'send-reminder': {
# #     # run this task every minute
# #     'task': 'apps.node_api.tasks.send_reminder',
# #     'schedule': crontab()
# #   },
# # }

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


