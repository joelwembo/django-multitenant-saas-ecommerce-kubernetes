# Creating App Inside Apps Parent app directory

 1. Inside apps folder create a new folder home as app

 2. python manage.py startapp home apps/home

 3. inside home On apps.py

 from django.apps import AppConfig


class FlightConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.flight'


python manage.py startapp users apps/users