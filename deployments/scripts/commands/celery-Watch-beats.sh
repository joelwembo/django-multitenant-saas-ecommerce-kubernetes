docker exec -it web_cloudapp_django celery -A fintechengine  beat -l INFO --logfile=celery.log
