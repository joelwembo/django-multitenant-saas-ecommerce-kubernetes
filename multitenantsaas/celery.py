# from __future__ import absolute_import, unicode_literals
# import os
# import random
# from celery import Celery , shared_task
# from celery.schedules import crontab

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multitenantsaas.settings")

# app = Celery("multitenantsaas")
# app.config_from_object("django.conf:settings", namespace="CELERY")
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# # app.conf.beat_schedule = {
# # # Executes every Monday morning at 7:30 a.m.
# # # 'send-reminder': {
# # #     # run this task every minute
# # #     'task': 'apps.node_api.tasks.send_reminder',
# # #     'schedule': crontab()
# # #   },
# # # }

# app.conf.beat_schedule = {
#     'multiply-task-crontab': {
#         'task': 'multiply_two_numbers',
#         # 'schedule': crontab(hour=7, minute=30, day_of_week=1),
#         'schedule': 45,
#         'args': (16, 16),
#     },
#     'multiply-every-5-seconds': {
#         'task': 'multiply_two_numbers',
#         'schedule': 60,
#         'args': (16, 16)
#     },
#     # 'add-every-30-seconds': {
#     #     # 'task': 'add',
#     #     'task': 'apps.finance.tasks.add',
#     #     'schedule': 60,
#     #     'args': (30, 20)
#     # },
# }


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
    
    


# @shared_task(name="sub_two_numbers")
# def sub(x, y):
#     # Celery recognizes this as the `multiple_two_numbers` task
#     total = x - y
#     return total




