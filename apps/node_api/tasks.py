from celery import shared_task
from django.core.mail import EmailMessage
from celery.utils.log import get_task_logger
from fintechengine.celery import app
from .models import SubscribeToNewsletter


logger = get_task_logger(__name__)

# @app.task
# def send_reminder():
#     # this will be used to send mail to all subscribed users
#     all_users = SubscribeToNewsletter.objects.all()
#     for user in all_users:
#         logger.info("Reminder message sent")
#         email = EmailMessage(
#                     subject= 'Reset your password',
#                     body=  'Hi, thank you for subscribing to our',
#                     to=[user.email]
#                  )
#         email.send(fail_silently=True)
#     return {'status': 'sent successfully'}


@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print("Test App Loading " , i)
    return "Done"


@shared_task(bind=True)
def run_func(self):
    #operations
    for i in range(10):
        print("Test App Processing" , i)
    return "Done"