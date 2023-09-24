# Django Rest API , Kubernetes, Jenkins, Github Actions and Multiple Databases
![image](https://github.com/joelwembo/Django-restful-api-postgres-kubernetes-poc/assets/19718580/d00f0e7d-050d-454c-8d6b-f8890eb1f506)

# Required Tools

- Docker
- Docker Compose
- Postgres
- Redis
- Celery
- Kubernetes
- Ansible

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers
python3 -m venv env 

# create a new virtual environemnt
source env/bin/activate   # For Windows use env\Scripts\activate

Install Django and Django REST framework into the virtual environment
pip install django 

pip install djangorestframework

Set up a new project with a single application
django-admin startproject tutorial . # Note the trailing '.' character cd tutorial django-admin startapp quickstart cd ..

Virtual Environment

# For Windows

(Project folder at the root folder with manage.py) python -m pip install --user virtualenv virtualenv env

for Lunix source env/bin/activate

For Windows env\Scripts\activate

The Env folder will propmt aside the path


# Postgres DB Connection
''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fintech_enterpriseDB',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
''
# Docker Database Settings

# Database postgres Docker 
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'fintech_enterpriseDB',
        'USER': 'postgres',
         'PASSWORD': 'postgres',
         'HOST': 'postgres',
         'PORT': 5432,
     }
 }

# Step 1

pip install django django-rest-framework djongo mysqlclient coverage

# Step 2
django-admin startproject tutorial . # Note the trailing '.' character cd tutorial django-admin startapp quickstart

# Data migration
python manage.py makemigrations python manage.py migrate

Creating an admin user

python manage.py createsuperuser or

python manage.py createsuperuser --database=pools specify the database

#Compiling

python manage.py runserver 0.0.0.0:8081

# Prepare Requirement doc for all tools and lib

 step 1 pip freeze 

 step 2 pip freeze > requirements.txt

# Managaning Multiple Database

# Loading Data

Data Inside Fixtures Folder

$ python manage.py loaddata restaurants

![image](https://github.com/joelwembo/Django-restful-api-postgres-kubernetes-poc/assets/19718580/7b4dc37b-3fc0-462f-a44a-28febddcf716)


# URLS
---------------------------------------------------------------------------------------------------------------

Entry point
http://127.0.0.1:8585/

Appview

http://localhost:8585/api/v1/notes/apiview
http://localhost:8585/api/v1/snippets/apiview

Snippets

http://127.0.0.1:8585/api/v1/snippets/
http://127.0.0.1:8585/api/v1/snippets/

Notes
http://localhost:8585/api/v1/notes/
http://localhost:8585/api/v1/notes/


# Swagger and APIDocs
http://127.0.0.1:8585/swagger/

# Docker Compilation

docker-compose down && docker-compose build --no-cache  && docker-compose up

- Docker Django shell

docker exec -it cloudapp-django-web bash
bash ./deployments/scripts/commands/docker-shell.sh

- Docker migration commands

bash ./deployments/scripts/commands/migrate.sh

docker exec -it cloudapp-django-web python manage.py makemigrations
docker exec -it cloudapp-django-web python manage.py migrate

- Docker celery commands

bash ./deployments/scripts/commands/celery-Watch-beats.sh  
bash ./deployments/scripts/commands/celery-watch-logs.sh

docker exec -it cloudapp-django-web celery -A fintechengine  beat -l INFO --logfile=celery.log

- Docker Create Super Users

bash ./deployments/scripts/commands/createsuperuser.sh

docker exec -it cloudapp-django-web python manage.py makemigrations
docker exec -it cloudapp-django-web python manage.py migrate

# Kubernetes Deployments

1. DOCKER_SCAN_SUGGEST=false docker build -t joelwembo/cloudapp-django-web .
2. docker run -d -p 80:80 --name django joelwembo/cloudapp-django-web:latest   
3. docker push joelwembo/cloudapp-django-web:latest
4. minikube start --driver=docker
5. kubectl create namespace cloudapp-django-web
6. kubectl config set-context --current --namespace=cloudapp-django-web
7. kubectl apply -f ./deployments/k8s/deployment.yaml
8. kubectl apply -f ./deployments/k8s/load-balancer.yaml
9. kubectl get services -w
9. minikube ip
10. kubectl scale deployment cloudapp-django-web --replicas=10

# Running Your Test Suite

$ pytest
$ pytest tests                          # test a directory
$ pytest test.py                        # test file
