docker exec -it web_cloudapp_django celery -A multitenantsaas  beat -l INFO --logfile=celery.log
