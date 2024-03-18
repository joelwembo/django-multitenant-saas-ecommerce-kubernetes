# django-multitenant-saas-ecommerce-kubernetes 

![image](https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes/assets/19718580/f52b4f26-b42f-4f16-81fc-3aac8cc62f82)

![image](https://github.com/joelwembo/django-restful-api-postgres-kubernetes-poc/assets/19718580/2a609fc0-be6e-42dd-b954-35dbb5776b60)

@author : Joel Otepa Wembo



# Automating Django , Celery, Redis and postgres deployment to AWS EC2 using Terraform ( Complete Guide) !

In this article, we will study how we can automate the deployment of our existing Django web application to Ubuntu Server in AWS EC2 Using terraform and CloudFormation. We will also see how to use the public IP of the EC2 instance to access the Django application. For this article, you should know about setting up EC2 in AWS. The Django application will be fully containerized along side with Celery, Redis, and Postgres. We have provided 2 options for you to deploy with postgres either using another docker container or by provisioning your postgres using AWS RDS for PostgreSQL. We will leverage both Terraform and Github actions to automate the deployment process, making it more efficient and error-free.
## Pre-requisites

Before we get into the good stuffs, first we need to make sure we have the required services on our local machine, which are:

Terraform
AWS CLI
AWS Account
Docker
Python 3
Github Account
Basic familiarity with YAML and GitHub workflows.
A Django project hosted in a GitHub repository.


# create a new virtual environemnt
virtualenv venv 

source ./venv/Scripts/activate ( Windows )
source ./venv/bin/activate ( ubuntu)

source ./venv/Scripts/deactivate

pip install -r requirements.txt

# Local 

python manage.py createsuperuser
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


# Multi tenant settings

pip install -r requirements.txt

python manage.py makemigrations finances
python manage.py makemigrations app

python manage.py migrate finances
python manage.py migrate app

tenant = Client(schema_name="test", name="test Company")

domain = Domain(domain="btest.localhost", tenant=tenant, is_primary=True)

# CI/CD Workflows

![1594373757598](https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes/assets/19718580/3e5502e5-94b8-4229-9f7f-505b7f445c8a)

- Tools
- Docker
- Jenkins
- Ubuntu
- Kubernetes
- Bash
- Python
- Terraform

# For more information contact: 

- @author : Joel Otepa Wembo
- @website: www.joelwembo.com
- @linkedin: https://www.linkedin.com/in/joelotepawembo/



