# Django Rest API , Kubernetes, Jenkins, Github Actions and Multiple Databases

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers
python3 -m venv env 

# Env Setup
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

# Step 1

pip install django django-rest-framework djongo mysqlclient coverage

# Step 1
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
