# Django-multitenant-saas-ecommerce-project
## Automating Django , Celery , Redis and postgres deployment to AWS EC2 using Terraform ( Complete Guide)

![image](https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes/assets/19718580/f52b4f26-b42f-4f16-81fc-3aac8cc62f82)


## Introduction
Automating deployment processes is crucial for modern web development, enhancing productivity and reliability. In this article, we focus on automating the deployment of a Django web application onto an Ubuntu Server hosted on AWS EC2.

Setting up the Environment: Before diving into deployment automation, it’s essential to have a solid understanding of setting up EC2 instances on AWS. We’ll guide you through this process to ensure a smooth transition into deployment automation.

Containerization and Infrastructure: Our Django application, along with Celery, Redis, and PostgreSQL, will be containerized, allowing for easy management and scalability. We discuss the advantages of containerization and how it facilitates deployment automation.

Deployment Options for PostgreSQL: We present two options for deploying PostgreSQL: using another Docker container or provisioning AWS RDS for PostgreSQL. We discuss the benefits and considerations of each approach to help you choose the one that best suits your requirements.

Automation with Terraform and CloudFormation: Terraform and CloudFormation are powerful tools for infrastructure as code (IaC). We demonstrate how to leverage these tools to automate the deployment process efficiently. From provisioning EC2 instances to configuring networking and security groups, we cover all aspects of infrastructure setup.

Integrating GitHub Actions: GitHub Actions offer seamless CI/CD capabilities, enabling automated workflows directly from your GitHub repository. We showcase how to integrate GitHub Actions into your deployment pipeline, ensuring continuous deployment with every code change.

Accessing the Django Application: Finally, we demonstrate how to access the deployed Django application using the public IP of the EC2 instance. We discuss best practices for managing access and securing your application in a production environment.

## Prerequisites:
Before we get into the good stuffs, first we need to make sure we have the required services on our local machine or dev server, which are:

Basic knowledge of Django
AWS Account
Github Account
AWS CLI installed and configured.
ECS CLI
Docker installed locally.
Typescript installed
Postman
Python 3
NPM
NodeJS
Terraform
A Domain name Hosted from any domain name provider ( Ex: AWS Route 53 )
Basic familiarity with YAML and GitHub workflows.
A Django project hosted in a GitHub repository
Basic knowledge of HTML or React
Any Browser for testing
Intermediate knowledge in Serverless Computing ( Ex : AWS Lambda , ECS,..)
You can follow along with this source code:
GitHub - joelwembo/django-multitenant-saas-ecommerce-kubernetes: Django Multi-tenant …
Django Multi-tenant , microservices , Kubernetes, Jenkins, Github Actions and Multiple Databases using docker, bash…
github.com



## Step 1: Create a virtual environment to hold all pip libraries installations

If you don’t have virtualenv installed, you can install it by running the following command in your CMD after Python was installed:

virtualenv venv
## Step 2 : Activate the environment:

source ./venv/bin/activate
source ./venv/bin/deactivate ( To Deactivate )

##Step 3: Create project folder

mkdir app
## Step 4: Install Django

pip install django
## Step 5: Create a new Django project inside the project folder

A Django app is a self-contained component of a Django project. It is a module that provides specific functionality, such as handling authentication, managing blog posts, or serving an API. An app should represent a single, specific functionality or purpose within the overall website.

django-admin startproject django-multitenant-saas-ecommerce-kubernetes
## Step 6: Create a new test app:

within the django project using the following command:

python manage.py startapp testapp
***Adding a new app into the project***

python manage.py startapp home apps/home

## Step 7 : Execute ORM Data Migrations:

python manage.py makemigrations
python manage.py migrate

## Step 8: Launch the django development server

python manage.py runserver


## Summary
Automating Django deployments using Terraform and GitHub Actions offers a streamlined and reliable way to manage application delivery.

By following the steps outlined above, developers can set up a robust deployment pipeline that pushes their latest “Dockerized” Django app images to an AWS EC2 instance seamlessly upon every push to the main branch.

“The quality, relevance, and impact of the products and services output by the technology sector can only be improved by having the people who are building them be demographically representative of the people who are using them.” — Tracy Chou, current CEO of Block Party, ex Pinterest, Quora

You can also find the codes on Github here.

Thank you for Reading !! 🙌🏻😁, see you in the next article. 📃




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


# For more information contact: 

- @author : Joel Otepa Wembo
- @website: www.joelwembo.com
- @linkedin: https://www.linkedin.com/in/joelotepawembo/



