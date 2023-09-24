
docker exec -it django_fintech_enterprise_container celery -A fintechengine worker -l INFO
docker exec -it django_fintech_enterprise_container celery -A fintechengine beat -l INFO
