import os
from pathlib import Path
import socket 
from decouple import config
from unipath import Path
from dotenv import load_dotenv
import datetime
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'. #
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY', default='54g6s%qjfnhbpw0zeoei=$!her*y(p%!&84rs$4l85io')
SECRET_KEY = config('SECRET_KEY', default = os.environ.get("DJANGO_SECRET_KEY", "54g6s%qjfnhbpw0zeoei=$!her*y(p%!&84rs$4l85io"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# if DEBUG:
#     hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#     INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2", "host.docker.internal"]
    
# ALLOWED_HOSTS = [os.getenv("ALLOWED_PORTS")]
ALLOWED_HOSTS = ['localhost' , '127.0.0.1', '0.0.0.0', 'host.docker.internal']

BACKEND_DOMAIN = 'http://127.0.0.1:8585/'
PAYMENT_SUCCESS_URL = 'http://127.0.0.1:8585/api/v1/products/success/'
PAYMENT_CANCEL_URL = 'http://127.0.0.1:8585/api/v1/products/cancel/'

CORS_ORIGIN_ALLOW_ALL = True
# Application definition # # # # #

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',
    'rest_framework',
    "corsheaders",
    'graphene_django',
    'django_celery_results',
    'django_celery_beat',
    'django_filters',
    'drf_yasg',
    'widget_tweaks',
    'apps.home',
    'apps.snippets',
    'apps.users',
    'apps.finances',
    'apps.payments',
    'apps.products',
    'data_browser',
    # 'django-ledger',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "host.docker.internal"
]

ROOT_URLCONF = 'fintechengine.urls'
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fintechengine.wsgi.application'

# Database # #
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }
# 
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Database postgres Docker 
# Docker host : host.docker.internal  or db cloudapp-django-postgresdb  3.0.55.190
# docker inspect cloudapp-django-postgresdb | grep "IPAddress"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_NAME", "DB1"),
        'USER': os.environ.get("POSTGRES_USER", "postgres"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "postgres"),
        'HOST': os.environ.get("POSTGRES_HOST", "localhost"),
        'PORT': int(os.environ.get("POSTGRES_PORT", "5432")),
    }
}

# Postgres DB Connection #
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get("POSTGRES_NAME", "postgres"),
#         'USER': os.environ.get("POSTGRES_USER", "postgres"),
#         'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "postgres"),
#         'HOST': os.environ.get("POSTGRES_HOST", "localhost"),
#         'PORT': int(os.environ.get("POSTGRES_PORT", "5432")),
#     }
# }

# #Production / Development MYSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DB1',
#         'USER': 'root',
#         'HOST': 'localhost',
#         'PASSWORD': '',
#         'PORT': '3306',
#     }
# }

# Docker Settings for Mysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DB1',
#         'USER': 'root',
#         'HOST': 'localhost',
#         'PASSWORD': '',
#         'PORT': '3306',
#     }
# }

#Connect to Neo4j Database
# config.DATABASE_URL = 'bolt://neo4j+s://f89c638e.databases.neo4j.io:7687'

# Password validation # #
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # ),
    
}
# # gh #

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

CORS_ALLOW_CREDENTIALS = True


# Internationalization #
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

IMAGES_DIR = os.path.join(MEDIA_ROOT, 'images')

if not os.path.exists(MEDIA_ROOT) or not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_PROFILE_MODULE = 'auth.User'

AUTH_USER_MODEL = 'auth.User'

# Extra places for collectstatic to find static files. #
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)


MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 2048

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get("BROKER_URL", "redis://localhost:6379/1"),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
# Django Data Browser
# References : https://pypi.org/project/django-data-browser/
DATA_BROWSER_FE_DSN = "https://af64f22b81994a0e93b82a32add8cb2b@o390136.ingest.sentry.io/5231151"


# Celery Settings and Redis  Production Setting # #
CELERY_BROKER_URL=os.environ.get("CELERY_BROKER", "redis://localhost:6379/0")
# CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND= os.environ.get("CELERY_RESULT_BACKEND", "db+postgresql://postgres:postgres@localhost/DB1")  # Use PostgreSQL as the result backend
BROKER_URL=os.environ.get("BROKER_URL", "redis://localhost:6379/1")
CELERY_ACCEPT_CONTENT=['application/json']
CELERY_TASK_SERIALIZER='json'
CELERY_RESULT_SERIALIZER='json'
CELERY_TIMEZONE="Asia/Singapore"
CELERY_TASK_TRACK_STARTED=True
CELERY_TASK_TIME_LIMIT=30 * 60
CELERY_TASK_ALWAYS_EAGER=True
CELERY_TASK_EAGER_PROPAGATES=True
CELERY_ALWAYS_EAGER=True
BROKER_HEARTBEAT = 10 
BROKER_HEARTBEAT_CHECKRATE = 2.0
BROKER_POOL_LIMIT = None
BROKER_CONNECTION_RETRY = False
BROKER_CONNECTION_MAX_RETRIES = 0
BROKER_CONNECTION_TIMEOUT = 120
BROKER_CONNECTION_RETRY_ON_STARTUP= True
BROKER_CHANNEL_ERROR_RETRY=True
# Configuration for sending email using gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS=os.environ.get("EMAIL_USE_TLS", True)
EMAIL_HOST=os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_HOST_USER=os.environ.get("EMAIL_HOST_USER", "notifyprodtestemail1@gmail.com")
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD", "Michael@5151")
EMAIL_PORT=os.environ.get("EMAIL_PORT", 587)

