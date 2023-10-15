
docker exec -it cloudapp-django-web python manage.py makemigrations
docker exec -it cloudapp-django-web python manage.py migrate

docker exec -it cloudapp-django-web python manage.py createsuperuser

