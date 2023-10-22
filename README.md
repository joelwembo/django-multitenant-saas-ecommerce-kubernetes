# DJANGO Cloud App

@author : Joel Otepa Wembo

# create a new virtual environemnt
virtualenv venv 

source ./venv/Scripts/activate

source ./venv/Scripts/deactivate

# Local 

bash ./server-entrypoint.sh

# Docke

bash ./run.sh

http://127.0.0.1:8585/

# API Docs

http://127.0.0.1:8585/swagger/

# Data Browser

http://127.0.0.1:8585/data-browser/

# GraphQL
http://127.0.0.1:8585/graphql

# Extensions
python manage.py show_urls
python manage.py graph_models finances -a -o finances_models.png

# wagtail

# Django ledger
pip install pipenv (globally)
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

pipenv install django-ledger[graphql,pdf]
python manage.py test django_ledger
