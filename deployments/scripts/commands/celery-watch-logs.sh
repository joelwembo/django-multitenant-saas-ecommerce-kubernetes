docker exec -it cloudapp-django_celery_1 celery -A fintechengine  worker -l INFO 

docker exec -it cloudapp-django_celery_1 celery -A fintechengine worker -l info --beat