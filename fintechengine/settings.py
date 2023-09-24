import os
from pathlib import Path
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
SECRET_KEY = config('SECRET_KEY', default=os.getenv("DJANGO_SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# ALLOWED_HOSTS = [os.getenv("ALLOWED_PORTS")]
ALLOWED_HOSTS = ['3.0.55.190', '0.0.0.0', '10.162.0.2', '127.0.0.1', 'localhost']

CORS_ORIGIN_ALLOW_ALL = True
# Application definition # # # # #

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "corsheaders",
    'django_celery_results',
     'django_celery_beat',
    'django_filters',
    'drf_yasg',
    'apps.snippets',
    'apps.users',
    'apps.node_api',
    'apps.finances',
    'apps.payments'
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
        'NAME': os.environ.get("POSTGRES_NAME", "postgres"),
        'USER': os.environ.get("POSTGRES_USER", "postgres"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "postgres"),
        'HOST': os.environ.get("POSTGRES_HOST", "host.docker.internal"),
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
#         'NAME': 'fintech_enterprisedb',
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
#         'NAME': 'fintech_enterpriseDB',
#         'USER': 'root',
#         'HOST': 'localhost',
#         'PASSWORD': '',
#         'PORT': '3306',
#     }
# }

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
    "http://localhost:3000",
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

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_PROFILE_MODULE = 'auth.User'

AUTH_USER_MODEL = 'auth.User'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)


MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 1024
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://redis:6379/1',  # Use Redis service hostname
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# Celery Settings and Redis  Production Setting # #
CELERY_BROKER_URL=os.environ.get("CELERY_BROKER", "redis://host.docker.internal:6379/0")
CELERY_RESULT_BACKEND = 'redis://host.docker.internal:6379/0'
# CELERY_RESULT_BACKEND = 'db+postgresql://postgres:postgres@postgres/postgres'  # Use PostgreSQL as the result backend
BROKER_URL = 'redis://host.docker.internal:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = "Asia/Singapore"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

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
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

