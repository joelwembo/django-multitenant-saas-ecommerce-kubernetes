# DJANGO Cloud App
![image](https://github.com/joelwembo/django-restful-api-postgres-kubernetes-poc/assets/19718580/2a609fc0-be6e-42dd-b954-35dbb5776b60)


@author : Joel Otepa Wembo

# create a new virtual environemnt
virtualenv venv 

source ./venv/Scripts/activate

source ./venv/Scripts/deactivate

# Multi tenant settings

pip install -r requirements.txt

python manage.py makemigrations client_app
python manage.py makemigrations app

python manage.py migrate client_app
python manage.py migrate app

tenant = Client(schema_name="bigco", name="Big Company")

domain = Domain(domain="bigco.localhost", tenant=tenant, is_primary=True)

# Local 

bash ./server-entrypoint.sh

# Docker

bash ./run.sh

http://127.0.0.1:8585/

# API Docs

http://127.0.0.1:8585/swagger/

# Data Browser

http://127.0.0.1:8585/data-browser/
![image](https://github.com/joelwembo/django-restful-api-postgres-kubernetes-poc/assets/19718580/83a0f788-36ea-4bb1-a626-17c2154bd512)


# GraphQL
![Alt text](image.png)
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
