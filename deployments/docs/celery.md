Starting the worker process
In a production environment you’ll want to run the worker in the background as a daemon - see Daemonization - but for testing and development it is useful to be able to start a worker instance by using the celery worker manage command, much as you’d use Django’s manage.py runserver:

$ celery -A proj worker -l INFO
For a complete listing of the command-line options available, use the help command:

$ celery help

# GET LOGS

 celery -A fintechengine worker -l INFO --logfile=celery.log --detach 
 
# django shell

from fintechengine.apps.home.tasks import print_message, print_time, calculate

from apps.home.tasks import print_message, print_time, calculate

  
print_message.delay("Hello World")  
print_time.delay()  
calculate.delay(10,20)