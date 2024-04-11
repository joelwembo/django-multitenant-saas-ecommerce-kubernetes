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

Prerequisites:
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

Why Terraform ?
Choosing Terraform for deploying a Django application on Amazon EC2 has several advantages like Infrastructure as Code (IaC), Multi-Cloud Support and ease of deployment. Terraform provides a robust and scalable solution for deploying Django applications on EC2, offering benefits such as automation, repeatability, scalability, and ease of management.

1. Let Start with Django
Django is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established in the US as a 501 non-profit.


Django
Make sure you have the following prerequisites installed on your Windows machine or ubuntu server to follow the instructions:

Python 3.6 or higher (download)
virtualenv
Docker
We will use the built-in Command Prompt (CMD) for this tutorial. You can search for CMD to open it using Windows search.

Step 1: Create a virtual environment to hold all pip libraries installations

If you don’t have virtualenv installed, you can install it by running the following command in your CMD after Python was installed:

virtualenv venv
Step 2 : Activate the environment:

source ./venv/bin/activate
source ./venv/bin/deactivate ( To Deactivate )
Step 3: Create project folder

mkdir app
Step 4: Install Django

pip install django
Step 5: Create a new Django project inside the project folder

A Django app is a self-contained component of a Django project. It is a module that provides specific functionality, such as handling authentication, managing blog posts, or serving an API. An app should represent a single, specific functionality or purpose within the overall website.

django-admin startproject django-multitenant-saas-ecommerce-kubernetes
Step 6: Create a new test app:

within the django project using the following command:

python manage.py startapp testapp
***Adding a new app into the project***

python manage.py startapp home apps/home

Step 7 : Execute ORM Data Migrations:

python manage.py makemigrations
python manage.py migrate
Step 8: Launch the django development server

python manage.py runserver

Running django server
2. Dockerize the Django application
Docker is a popular platform for developing, shipping, and running applications.

Here are some key reasons why Docker is widely used:

Portability: Docker containers encapsulate the application, along with all its dependencies, into a single package. This package can run on any system that supports Docker, regardless of the underlying infrastructure. This portability makes it easy to move applications between environments, such as development, testing, and production, without worrying about differences in the underlying system configuration.
Consistency: Docker ensures that the environment in which the application runs is consistent across different machines. Developers can specify the exact dependencies and configuration required for their application using Dockerfiles and Docker Compose files. This consistency reduces the likelihood of bugs and compatibility issues caused by differences between development and production environments.
Isolation: Docker containers provide a high degree of isolation between applications and the underlying system. Each container runs as a separate process, with its own filesystem, network, and process space. This isolation improves security by limiting the impact of any vulnerabilities in one application on other applications running on the same system.
Resource Efficiency: Unlike traditional virtual machines, Docker containers share the host system’s kernel, which makes them lightweight and consumes fewer resources. Multiple containers can run on the same host without significant overhead, allowing for efficient resource utilization and scalability.
Scalability: Docker’s architecture makes it easy to scale applications horizontally by running multiple instances of the same container across different hosts or on a container orchestration platform like Kubernetes. This scalability enables applications to handle increased workload and traffic without manual intervention.
Continuous Integration and Deployment (CI/CD): Docker simplifies the process of building, testing, and deploying applications through automation. Developers can use Docker images to create consistent build environments, run automated tests inside containers, and deploy applications as immutable infrastructure. This CI/CD pipeline improves development velocity and enables faster release cycles.
Microservices Architecture: Docker is well-suited for building microservices-based architectures, where applications are composed of small, loosely coupled services that can be developed, deployed, and scaled independently. Each microservice can run in its own container, making it easier to manage and update individual components of the application without affecting the entire system.
Overall, Docker provides developers and organizations with a flexible, efficient, and scalable platform for building, deploying, and managing applications in various environments.

Dockerizing a Django application with PostgreSQL involves creating Docker containers for both Django and PostgreSQL, and then configuring them to work together. Below are the steps to dockerize a Django application with PostgreSQL:

Step 1: Dockerfile for Django Application: Create a Dockerfile in the root directory of your Django project. This file will define the configuration for building the Docker image for your Django application. Here's a basic example:

# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file into the container at /app
COPY requirements.txt /app/
COPY gunicorn-cfg.py /app/
# COPY deployments ./app/deployments/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
# RUN pip install django-filter
# Copy the current directory contents into the container at /app
COPY . /app/
EXPOSE 8585
Step 2: docker-compose.yml:

Create a docker-compose.yml file in the root directory of your project. This file defines the services, networks, and volumes for your Docker containers.

version: "3.9"
services:
  web:
    image: django_app
    container_name: cloudapp-django-web
    env_file: .env
    restart: always
    build:
      context: .
      dockerfile: Dockerfile
    command:
      - /bin/sh
      - -c
      - |
        python manage.py migrate
        python manage.py runserver 0.0.0.0:8585     
    ports:
      - "8585:8585"
    networks:
      - web_network
    volumes:
       - appdata:/app
    depends_on:
      - cloudapp-django-postgresdb
      - redis 
    deploy:
      resources:
        limits:
          cpus: '0.001'
          memory: 50M
        reservations:
          cpus: '0.0001'
          memory: 20M 
  celery:
    container_name: cloudapp-django-celery
    build: .
    command: 
       - /bin/sh
       - -c
       - |
        user=django
        group=developers
        environment=C_FORCE_ROOT="yes"
        environment=HOME="/root",USER="django"
        celery -A multitenantsaas worker -l info
        
    volumes:
      - .:/django_app
    environment:
      - DEBUG=0
      - DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 172.104.60.217  [::1]
      - CELERY_BROKER_URL="redis://redis:6379/0"
      - CELERY_RESULT_BACKEND="redis://redis:6379/0"
      - broker_connection_retry_on_startup="True"
      - CELERY_TASK_ALWAYS_EAGER=True
      - C_FORCE_ROOT=true
      - BROKER_TRANSPORT="kombu.transport.django"
    depends_on:
      - redis
  redis:
      image: "redis:alpine"
      container_name: cloudapp-django-redis
      ports:
        - '6379:6379'
      expose:
        - "6379"  
      volumes:
          - redisDB:/data
      # networks:
      #     - db_network  #
  cloudapp-django-postgresdb:
    restart: always
    image: postgres:latest
    container_name: cloudapp-django-postgresdb
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=DB2
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_PORT=5432
      - "POSTGRES_HOST_AUTH_METHOD=trust"
    expose:
       - "5432"
    ports:
       - "5432:5432"
    # networks:
    #    - data_network   
  pgadmin:
        restart: always
        image: dpage/pgadmin4
        container_name: cloudapp-fintech-pgadmin 
        depends_on:
          - cloudapp-django-postgresdb
        ports:
          - "5051:80"
        environment:
          PGADMIN_DEFAULT_EMAIL: 19718580.dev1@protonmail.com
          PGADMIN_DEFAULT_PASSWORD: postgres   
          PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION: 'False'
          PGADMIN_CONFIG_WTF_CSRF_CHECK_DEFAULT: 'False'

networks:
  web_network:
    driver: bridge
volumes:
  pgdata:
  redisDB:
  appdata:
   driver: local
Step 3: define the .env to save the development environment variables

SERVER=https://cloudapp.io
DEBUG=True
SECRET_KEY=
DJANGO_SECRET_KEY=%jjnu7=
DJANGO_SUPERUSER_PASSWORD=
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_USERNAME=joelwembo
ALLOWED_PORTS=localhost
POSTGRES_NAME=DB2
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
# POSTGRES_HOST=host.docker.internal
# POSTGRES_HOST=localhost
POSTGRES_HOST=cloudapp-django-postgresdb
Let first Launch the development server locally by using Make file

Makefiles are used to help decide which parts of a large program need to be recompiled. In the vast majority of cases, C or C++ files are compiled.

ifndef VERBOSE
MAKEFLAGS += --no-print-directory
endif
SHELL := /bin/bash
.DEFAULT_GOAL := help

DOCKER_USERNAME ?= joelwembo
APPLICATION_NAME ?= saas-ecommerce-kubernetes
GIT_HASH ?= $(shell git log --format="%h" -n 1)


help:
 @ echo "Use one of the following targets:"
 @ tail -n +8 Makefile |\
 egrep "^[a-z]+[\ :]" |\
 tr -d : |\
 tr " " "/" |\
 sed "s/^/ - /g"
 @ echo "Read the Makefile for further details"


venv virtualenv:
 @ echo "Creating a new virtualenv..."
 @ rm -rf venv || true
 @ python3.11 -m venv venv
 @ echo "Done, now you need to activate it. Run:"
 @ echo "source venv/bin/activate"

activate:
 @ echo "Activating this python3.11 Virtual venv Env:"
 @ bash --rcfile "./venv/bin/activate"


requirements pip:
 @ if [ -z "${VIRTUAL_ENV}" ]; then \
  echo "Not inside a virtualenv."; \
  exit 1; \
 fi
 @ echo "Upgrading pip..."
 @ python3.11 -m pip install --upgrade pip
 @ echo "Updating pip packages:"
 @ pip install -r "requirements.txt"
 @ echo "Self installing this package in edit mode:"
 # @ pip install -e .
 @ echo "All pip libraries installed You are ready to go ;-)"


requirementsdev:
 @ if [ -z "${VIRTUAL_ENV}" ]; then \
  echo "Not inside a virtualenv."; \
  exit 1; \
 fi
 @ echo "Upgrading pip..."
 # @ python3.11 -m pip install --upgrade pip
 @ echo "Updating pip packages:"
 @ pip install -r "requirements_dev.txt"


cleanfull:
 @ echo "Cleaning old files..."
 @ rm -rf **/.pytest_cache
 @ rm -rf .tox
 @ rm -rf dist
 @ rm -rf build
 @ rm -rf **/__pycache__
 @ rm -rf *.egg-info
 @ rm -rf .coverage*
 @ rm -rf **/*.pyc
 @ rm -rf env
 @ rm -rf venv
 @ rm -rf local
 @ rm -rf .aws-sam
 @ echo "All done!"

clean:
 @ echo "Cleaning old files..."
 @ rm -rf **/.pytest_cache
 @ rm -rf .tox
 @ rm -rf dist
 @ rm -rf build
 @ rm -rf **/__pycache__
 @ rm -rf *.egg-info
 @ rm -rf .coverage*
 @ rm -rf **/*.pyc
 @ echo "All done!"

start-engine:
 @ python3.11 manage.py makemigrations
 @ python3.11 manage.py migrate
 @ python3.11 manage.py runserver 0.0.0.0:8585


build:

 @ docker build --tag ${DOCKER_USERNAME}/${APPLICATION_NAME} .

push:
 @ docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}

docker-run:
 @ docker-compose down 
 @ docker-compose build --no-cache
 @ docker-compose up

release:
 @ docker pull ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH}
 @ docker tag  ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH} ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest
 @ docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest

Docker Compose

To view the Django app , open your browser and type the 127.0.0.1:8585


Django Rest Framework Viewset




Pgadmin4 credentials in docker-compose.yaml
You can access your pgadmin4 using https://localhost:5051/browser , we have docker-compose to provision both postgres and pgadmin4 as follow as side with another option of using AWS RDS for postgres as follows:

cloudapp-django-postgresdb:
    restart: always
    image: postgres:latest
    container_name: cloudapp-django-postgresdb
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=DB2
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_PORT=5432
      - "POSTGRES_HOST_AUTH_METHOD=trust"
    expose:
       - "5432"
    ports:
       - "5432:5432"
    # networks:
    #    - data_network   
  pgadmin:
        restart: always
        image: dpage/pgadmin4
        container_name: cloudapp-fintech-pgadmin 
        depends_on:
          - cloudapp-django-postgresdb
        ports:
          - "5051:80"
        environment:
          PGADMIN_DEFAULT_EMAIL: 19718580.dev1@protonmail.com
          PGADMIN_DEFAULT_PASSWORD: postgres   
          PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION: 'False'
          PGADMIN_CONFIG_WTF_CSRF_CHECK_DEFAULT: 'False'

pgadmin4 using docker-compose
3. Create AWS Access Keys
AWS access keys are credentials used to access Amazon Web Services (AWS) programmatically. They consist of an access key ID and a secret access key. These keys are used to authenticate requests made to AWS services via APIs, SDKs, command-line tools, and other means.

Steps to Create Access Keys

Go to the AWS management console, click on your Profile name, and then click on My Security Credentials. …
Go to Access Keys and select Create New Access Key. …
Click on Show Access Key and save/download the access key and secret access key.



4. AWS EC2 Provisioning Using Terraform and Github Actions
In this step, we are going to automate the provisioning of ubuntu ec2 server using terraform and GitHub actions.

GitHub Actions is a feature provided by GitHub that allows you to automate various tasks within your software development workflows directly from your GitHub repository. It enables you to build, test, and deploy your code directly within GitHub’s ecosystem.

Now, let’s setup our AWS environment. We will be using Terraform to create our infrastructure. We will be creating the following main resources:

Amazon EC2
Amazon S3
IAM roles and policies
Let’s first create files that we plan to use in our terraform/ directory.


Project Folder Structure
First, let setup our GitHub Actions and Environment settings

On GitHub.com, navigate to the main page of the repository.
Under your repository name, click Settings. …
In the “Security” section of the sidebar, select Secrets and variables, then click Actions.
Click the Secrets tab.
Click New repository secret.





How to setup Repository secrets in Github for Github Actions
4. Create S3 Buckets to manager our terraform states

Next, let manually create s3s bucket folders for our states management during terraform workflows and GitHub.


S3 Bucket for terraform state

State Keeping with S3
We can also, provision s3 bucket using aws command line or CloudFormation:

aws s3api create-bucket --bucket django-app-8 --region ap-southeast-1
aws s3api create-bucket --bucket django-terraform-rds-1 --region ap-southeast-1
5. Create a Key Pairs
Next, create a key pair using Amazon EC2 · In the navigation pane, under Network & Security, choose Key Pairs. · Choose Create key pair. · For Name, enter a descriptive




Key pair list
Key-Pairs are necessary for accessing your EC2 instances using terminal/shell, especially Linux-based instances. You can also create your key pairs using aws cli command

To create a key-pair using AWS CLI, type aws ec2 create-key-pair — key-name <your_key_name>, where <your_key_name> is your key’s name by which it would be saved in the AWS. The output for the same is shown below, which is in the json format.

aws ec2 create-key-pair --key-name prodxcloud_test_key.pem

6. backend.tf
In Terraform, the backend is the component responsible for storing and retrieving Terraform state files, which contain information about your infrastructure and the resources managed by Terraform. The state file maintains a mapping between the resources in your configuration and the real-world resources they represent, enabling Terraform to manage and update your infrastructure accurately.

6.1 S3 bucket for terraform state management
Just verify first that the bucket where you are going to save the terraform state was already created.

terraform {
  backend "s3" {
    bucket         = "django-app-8"
    region         = "ap-southeast-1"
    key            = "state/terraform.tfstate"
    dynamodb_table = "data_onents_tf_lockid"
    encrypt        = true
  }
}
The code above ensure that state of our terraform resources are kept in s3 folder.

Or, you have another option to keep your state and runs at the same place using terraform cloud.

6.2 Terraform Cloud Configuration

Terraform Cloud
HashiCorp provides GitHub Actions that integrate with the Terraform Cloud API. These actions let you create your own custom CI/CD workflows to meet the needs of your organization.


Step 1: Create your project and workplace in terraform cloud


Create project in terraform Cloud

Step 2: Define Variables set to allow terraform cloud for state management


Step 3 : Change the default execution Mode to remote


Step 4 : Create API tokens for Github actions to interact with Terraform Cloud


Terraform cloud API tokens

API Token for your project

Generated Token

Organization token ( Optional )
7. provider.tf
Let define the terraform provider

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.52.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  access_key = var.access_key
  secret_key = var.secret_key
}
8. Define a file main.tf
Inside the same folder, define a file main.tf for resources definitions , edit your VPC , Subnets and ami accordingly.

You can get the both the VPC ID and subnets details in AWS Management Console:


Pre-Created VPC and Subnet Settings

VPC Details
# Terraform provision AWS EC2 instance with Terraform Cloud Management

variable "awsprops" {
  type = map(any)
  default = {
    region       = "ap-southeast-1"
    vpc          = "vpc-0002de108b3a9fab7"
    ami          = "ami-03caf91bb3d81b843"
    itype        = "t2.micro"
    subnet       = "subnet-04bd8587390d17dda"
    publicip     = true
    keyname      = "prodxsecure"
    secgroupname = "prodxcloud-aws-ec2-lab-1"
  }
}


// AMI Security group setting using HashiCorp Configuration Language (HCL)
resource "aws_security_group" "prod-sec-sg" {
  name        = var.instance_secgroupname
  description = var.instance_secgroupname
  vpc_id      = var.instance_vpc_id

  // To Allow SSH Transport

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      description = lookup(ingress.value, "description", null)
      from_port   = lookup(ingress.value, "from_port", null)
      to_port     = lookup(ingress.value, "to_port", null)
      protocol    = lookup(ingress.value, "protocol", null)
      cidr_blocks = lookup(ingress.value, "cidr_blocks", null)
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }


  tags = {
    Name = "allow_tls"
  }

  lifecycle {
    create_before_destroy = true
  }
}


# instance identity
resource "aws_instance" "project-iac" {
  ami                         = lookup(var.awsprops, "ami")
  instance_type               = lookup(var.awsprops, "itype")
  subnet_id                   = lookup(var.awsprops, "subnet") #FFXsubnet2
  associate_public_ip_address = lookup(var.awsprops, "publicip")
  key_name                    = lookup(var.awsprops, "keyname")


  vpc_security_group_ids = [
    aws_security_group.prod-sec-sg.id
  ]
  root_block_device {
    delete_on_termination = true
    volume_size           = 50
    volume_type           = "gp2"
  }
  tags = {
    Name        = "prodxcloud-aws-ec2-lab-1"
    Environment = "DEV"
    OS          = "UBUNTU"
    Managed     = "PRODXCLOUD"
  }

  provisioner "file" {
    source      = "installer.sh"
    destination = "/tmp/installer.sh"

  }

  provisioner "remote-exec" {
    inline = [
      "sudo chmod +x /tmp/installer.sh",
      "sh /tmp/installer.sh"
    ]

  }
  depends_on = [aws_security_group.prod-sec-sg]


  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ubuntu"
    private_key = file("./prodxsecure.pem")
  }
}


output "ec2instance" {
  value = aws_instance.project-iac.public_ip
}

9. Run Github Actions Pipeline
To activate the github actions workflows, let define a file in ./github/workflows/terraform-aws-ec2–1.yaml

name: "Terraform Pipeline Provision EC2"

on:
 push:
   branches: ['master']
 pull_request:
   branches: ['master']

env:
 # verbosity setting for Terraform log
 TF_LOG: INFO
 # Credentials for deployment to AWS
 AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
 AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

 CONFIG_DIRECTORY: "./deployments/terraform/terraform-aws-ec2-s3/terraform/"

 
jobs:
 terraform:
   name: "Terraform Pipeline Provision EC2 with S3 Bucket"
   runs-on: ubuntu-latest
   defaults:
     run:
       shell: bash
       # We keep Terraform files in the terraform directory.
       working-directory: ./deployments/terraform/terraform-aws-ec2-s3/terraform
 
   steps:
     - name: Checkout the repository to the runner
       uses: actions/checkout@v2
 
     - name: Setup Terraform with specified version on the runner
       uses: hashicorp/setup-terraform@v2
       with:
         terraform_version: 1.3.0
    
     - name: Terraform init 
       id: init
       run: terraform init -lock=false
 
     - name: Terraform format
       id: fmt
       run: terraform fmt
    
     - name: Terraform validate
       id: validate
       run: terraform validate
 
     - uses: actions/github-script@v6
       if: github.event_name == 'pull_request'
       env:
         PLAN: "terraform\n${{ steps.plan.outputs.stdout }}"
       with:
         script: |
           const output = `#### Terraform Format and Style 🖌\`${{ steps.fmt.outcome }}\`
           #### Terraform Initialization ⚙️\`${{ steps.init.outcome }}\`
           #### Terraform Validation 🤖\`${{ steps.validate.outcome }}\`
           #### Terraform Plan 📖\`${{ steps.plan.outcome }}\`
 
           <details><summary>Show Plan</summary>
 
           \`\`\`\n
           ${process.env.PLAN}
           \`\`\`
 
           </details>
           *Pushed by: @${{ github.actor }}, Action: \`${{ github.event_name }}\`*`;
 
           github.rest.issues.createComment({
             issue_number: context.issue.number,
             owner: context.repo.owner,
             repo: context.repo.repo,
             body: output
           })
 
     - name: Terraform Plan Status
       if: steps.plan.outcome == 'failure'
       run: exit 1
 
     - name: Terraform Apply
      #  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
       run: terraform apply -auto-approve -input=false -lock=false

EC2 Instance IP address Allocated
10. Check result in your AWS Management Console

EC2 Creation Complete

EC2 Instance Connection Options

Access EC2 Using SSH

11. Provision AWS RDS for PostgreSQL using terraform
PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.

Aurora Serverless v1 is available for both Amazon Aurora with MySQL compatibility and Amazon Aurora with PostgreSQL compatibility. It’s easy to get started: choose Serverless when creating your Aurora database cluster, optionally specify the desired range of database capacity, and connect your applications.

Here is the code to provision the aws rds postgres using terraform

  
terraform {
  backend "s3" {
    bucket         = "django-terraform-rds-1"
    region         = "ap-southeast-1"
    key            = "state/terraform.tfstate"
    dynamodb_table = "mycomponents_tf_lockid"
    encrypt        = true
  }
}

provider "aws" {
    region = "ap-southeast-1"
  }

resource "aws_db_parameter_group" "education" {
  name   = "education"
  family = "postgres13"

  parameter {
    name  = "log_connections"
    value = "1"
  }
}

resource "aws_db_instance" "education" {
  identifier             = "education"
  instance_class         = "db.t3.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "13"
  username               = "postgres"
  password               = "postgres"
  parameter_group_name   = aws_db_parameter_group.education.name
  publicly_accessible    = true
  skip_final_snapshot    = true
}

output "rds_hostname" {
  description = "RDS instance hostname"
  value       = aws_db_instance.education.address
  sensitive   = true
}

output "rds_port" {
  description = "RDS instance port"
  value       = aws_db_instance.education.port
  sensitive   = true
}

output "rds_username" {
  description = "RDS instance root username"
  value       = aws_db_instance.education.username
  sensitive   = false
}
12. Push the changes and Run Github Actions Pipeline
To activate the github actions workflows, let define a file in ./github/workflows/terraform-rds-postgres.yaml

name: "Terraform Pipeline AWS RDS Postgres"
 
on:
 push:
   branches: ['master']
 pull_request:
   branches: ['master']

env:
 TF_LOG: INFO
 # Credentials for deployment to AWS
 AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
 AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
 # S3 bucket for the Terraform state
 #  BUCKET_TF_STATE: ${{ secrets.BUCKET_TF_STATE}}

 CONFIG_DIRECTORY: "./deployments/terraform/terraform-provision-aws-rds-postgres/terraform/"

 
jobs:
 terraform:
   name: "Terraform Pipeline AWS RDS Postgres"
   runs-on: ubuntu-latest
   defaults:
     run:
       shell: bash
       # We keep Terraform files in the terraform directory.
       working-directory: ./deployments/terraform/terraform-provision-aws-rds-postgres/terraform
 
   steps:
     - name: Checkout the repository to the runner
       uses: actions/checkout@v2
 
     - name: Setup Terraform with specified version on the runner
       uses: hashicorp/setup-terraform@v2
       with:
         terraform_version: 1.3.0
    
     - name: Terraform init 
       id: init
       run: terraform init -lock=false
 
     - name: Terraform Apply
      #  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
       run: terraform apply -auto-approve -input=false -lock=false
     
#     #  - name: Terraform Destroy All Resources
#     #    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
#     #    run: terraform destroy -auto-approve -input=false -lock=false


Github Actions and Terraform results on RDS provisioning


We get the RDS endpoint by looking at connectivity tab


RDS Host Credentials
Let test the access of our rds !

You can use the Amazon RDS console to simplify setting up a connection between an Amazon Elastic Compute Cloud (Amazon EC2) instance and a DB instance. Often, your DB instance is in a private subnet and your EC2 instance is in a public subnet within a VPC. You can use a SQL client on your EC2 instance to connect to your DB instance . The EC2 instance can also run web servers or applications that access your private DB instance .

Automatically connecting an EC2 instance and a DB instance by Joel Otepa Wembo
Automatically connecting an EC2 instance and a DB instance


automatic connectivity with an EC2 instance
13. Setup CI/CD pipelines for our Django app to aws ec2 using GitHub actions
Quick Note ! We already have docker and docker-compose installed in our aws ec2 during terraform provisioning using the file terraform-aws-ec2-s3/terraform/install.sh

sudo apt install apt-transport-https ca-certificates curl software-properties-common --assume-yes
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable'
apt-cache policy docker-ce
sudo apt install docker-ce --assume-yes
sudo chmod 777 /var/run/docker.sock

# sudo systemctl status docker
echo 'Docker successfully installer'

# install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
echo "Docker Compose Installed successfully installer"
For Your Github actions to access your aws ec2 instance, add your SSH private key in Github Settings.


AWS Private Key for AWS EC2 Access
Let Compose our deploy.yaml file inside the .github/workflows to deploy the test, build and deploy our django app to aws ec2.

name: Build Django Application

on:
  push:
    branches: ['master']
  pull_request:
    branches: [ "master" ]

env:
  DOCKERHUB_USERNAME: ${{ secrets.DOCKER_USER }}
  DOCKERHUB_TOKEN: ${{ secrets.DOCKER_PASSWORD }}
  AWS_PRIVATE_KEY: ${{ secrets.AWS_PRIVATE_KEY }}    

jobs:
  django_test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: .
    env:
      DJANGO_SECRET_KEY: 54g6s%qjfnhbpw0zeoei=$!her*y(p%!&84rs$4l85io
      POSTGRES_DB: DB2
      POSTGRES_PASSWORD: postgres
      POSTGRES_USER: postgres
      POSTGRES_HOST: localhost
      POSTGRES_PORT: 5432
      DB_IGNORE_SSL: "true"
    services:
      postgres_main:
        image: postgres:13
        env:
          POSTGRES_DB: ${{ env.POSTGRES_DB }}
          POSTGRES_USER: ${{ env.POSTGRES_USER }}
          POSTGRES_PASSWORD: ${{ env.POSTGRES_PASSWORD }}
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready 
          --health-interval 10s 
          --health-timeout 5s 
          --health-retries 5
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.9]
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      # - name: Install Dependencies
      #   run: |
      #     python -m pip install --upgrade pip
      #     pip install -r requirements.txt
      # - name: Run Tests
      #   run: |
      #       python --version

  build-and-push:
      name: Build Docker image and push to repositories
      needs: django_test
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v3

        - name: Set up Docker Buildx
          id: buildx
          uses: docker/setup-buildx-action@v2

        - name: Login to DockerHub
          uses: docker/login-action@v2
          with:
            username: ${{ env.DOCKERHUB_USERNAME }}
            password: ${{ env.DOCKERHUB_TOKEN }}

        - name: Build and push Docker image
          uses: docker/build-push-action@v2
          with:
            context: ./
            push: true
            dockerfile: ./Dockerfile
            tags: joelwembo/cloudapp-django-web:latest

  deploy-to-aws-ec2:
      needs: build-and-push
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v2
        - name: Login to Docker Hub
          uses: docker/login-action@v2
          with:
            username: ${{ env.DOCKERHUB_USERNAME }}
            password: ${{ env.DOCKERHUB_TOKEN }}
        
        - name: Set permissions for private key
          run: |
            echo "${{ env.AWS_PRIVATE_KEY }}" > prodxsecure.pem
            chmod 600 prodxsecure.pem
        - name: Pull Docker image
          run: |
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker pull joelwembo/cloudapp-django-web:latest'
        - name: Stop running container
          run: |
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker stop cloudapp-django-web || true'
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker rm cloudapp-django-web || true'
        - name: Run new container
          run: |
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker run -d --name cloudapp -p 8585:8585 joelwembo/cloudapp-django-web:latest'          

You will have the change the following part of the code to match with your instance IP address , username and key pair name and value :

        - name: Set permissions for private key
          run: |
            echo "${{ env.AWS_PRIVATE_KEY }}" > prodxsecure.pem
            chmod 600 prodxsecure.pem
        - name: Pull Docker image
          run: |
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker pull joelwembo/cloudapp-django-web:latest'
        - name: Stop running container
          run: |
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker stop cloudapp-django-web || true'
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker rm cloudapp-django-web || true'
        - name: Run new container
          run: |
            ssh -o StrictHostKeyChecking=no -i prodxsecure.pem ubuntu@47.128.216.140 'sudo docker run -d --name cloudapp -p 8585:8585 joelwembo/cloudapp-django-web:latest'

Testing Django


Django Workflows Completed
14. Check your application running live !
Finally, we can test the app in the production !

Start the server to test the application. Note down the address at which the server is started by default it is 127.0.0.1:8000. you will need to change that base upon your IP address.




Summary
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



