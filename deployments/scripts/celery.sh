celery -A fintechengine worker -l info
celery -A fintechengine beat -l info

celery -A fintechengine worker -l info --beat
