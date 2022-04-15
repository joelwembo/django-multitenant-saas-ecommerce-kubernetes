# Django Rest API and Multiple Databases

python3 -m venv env 

# Env Setup
source env/bin/activate   # For Windows use env\Scripts\activate

Install Django and Django REST framework into the virtual environment
pip install django 

pip install djangorestframework

Set up a new project with a single application
django-admin startproject tutorial . # Note the trailing '.' character cd tutorial django-admin startapp quickstart cd ..

Virtual Environment

#For Windows

(Project folder at the root folder with manage.py) python -m pip install --user virtualenv virtualenv env

for Lunix source env/bin/activate

For Windows env\Scripts\activate

The Env folder will propmt aside the path

next step

pip install django django-rest-framework djongo mysqlclient coverage

django-admin startproject tutorial . # Note the trailing '.' character cd tutorial django-admin startapp quickstart

Data migation
python manage.py makemigrations python manage.py migrate

Creating an admin user

python manage.py createsuperuser or

python manage.py createsuperuser --database=pools specify the database

running

python manage.py runserver 0.0.0.0:8081

Prepare Requirement doc for all tools and lib

# step 1 pip freeze 

# step 2 pip freeze > requirements.txt

Managaning Multiple Database


python manage.py makemigrations --database=core
python manage.py migrate --database=core

django-admin help¶
Run django-admin help to display usage information and a list of the commands provided by each application.

Run django-admin help --commands to display a list of all available commands.

Run django-admin help <command> to display a description of the given command and a list of its available options.

App names¶
Many commands take a list of “app names.” An “app name” is the basename of the package containing your models. For example, if your INSTALLED_APPS contains the string 'mysite.blog', the app name is blog.

Determining the version¶
django-admin version¶
Run django-admin version to display the current Django version.

The output follows the schema described in PEP 440:

1.4.dev17026
1.4a1
1.4
Displaying debug output¶
Use --verbosity, where it is supported, to specify the amount of notification and debug information that django-admin prints to the console.

Available commands¶
check¶
django-admin check [app_label [app_label ...]]¶
Uses the system check framework to inspect the entire Django project for common problems.

By default, all apps will be checked. You can check a subset of apps by providing a list of app labels as arguments:

django-admin check auth admin myapp
--tag TAGS, -t TAGS¶
The system check framework performs many different types of checks that are categorized with tags. You can use these tags to restrict the checks performed to just those in a particular category. For example, to perform only models and compatibility checks, run:

django-admin check --tag models --tag compatibility
--database DATABASE¶
Specifies the database to run checks requiring database access:

django-admin check --database default --database other
By default, these checks will not be run.

--list-tags¶
Lists all available tags.

--deploy¶
Activates some additional checks that are only relevant in a deployment setting.

You can use this option in your local development environment, but since your local development settings module may not have many of your production settings, you will probably want to point the check command at a different settings module, either by setting the DJANGO_SETTINGS_MODULE environment variable, or by passing the --settings option:

django-admin check --deploy --settings=production_settings
Or you could run it directly on a production or staging deployment to verify that the correct settings are in use (omitting --settings). You could even make it part of your integration test suite.

--fail-level {CRITICAL,ERROR,WARNING,INFO,DEBUG}¶
Specifies the message level that will cause the command to exit with a non-zero status. Default is ERROR.

compilemessages¶
django-admin compilemessages¶
Compiles .po files created by makemessages to .mo files for use with the built-in gettext support. See Internationalization and localization.

--locale LOCALE, -l LOCALE¶
Specifies the locale(s) to process. If not provided, all locales are processed.

--exclude EXCLUDE, -x EXCLUDE¶
Specifies the locale(s) to exclude from processing. If not provided, no locales are excluded.

--use-fuzzy, -f¶
Includes fuzzy translations into compiled files.

Example usage:

django-admin compilemessages --locale=pt_BR
django-admin compilemessages --locale=pt_BR --locale=fr -f
django-admin compilemessages -l pt_BR
django-admin compilemessages -l pt_BR -l fr --use-fuzzy
django-admin compilemessages --exclude=pt_BR
django-admin compilemessages --exclude=pt_BR --exclude=fr
django-admin compilemessages -x pt_BR
django-admin compilemessages -x pt_BR -x fr
--ignore PATTERN, -i PATTERN¶
Ignores directories matching the given glob-style pattern. Use multiple times to ignore more.

Example usage:

django-admin compilemessages --ignore=cache --ignore=outdated/*/locale



