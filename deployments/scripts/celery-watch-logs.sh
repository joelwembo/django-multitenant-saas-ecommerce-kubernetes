docker exec -it cloudapp-django_celery_1 celery -A multitenantsaas  worker -l INFO 

docker exec -it cloudapp-django_celery_1 celery -A multitenantsaas worker -l info --beat