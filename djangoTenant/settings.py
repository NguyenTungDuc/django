"""
Django settings for djangoTenant project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c)s!-l^1)!m3@i#m5d^57@&22fx6300$+w+6k*vmqg#=#8+czj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'Manager',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoTenant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djangoTenant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
AUTH_USER_MODEL = 'Manager.UserBase'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangoTenant',
        'USER': 'postgres',
        'PASSWORD': 'softdev',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'UWASSESS01',
#         'USER': 'uwassess_admin',
#         'PASSWORD': 'adminpwd01',
#         'HOST': 'uwassess01.ca5syam88qk6.us-east-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Rest framework 
# http://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
    'PAGE_SIZE': 10,
    'PAGINATE_BY': 10,  # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 10,  # Maximum limit allowed when using `?page_size=xxx`.


    # Render data
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
SITE_URL = "http://hiefficiencybar.com"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = SITE_URL+"/static/" 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = SITE_URL+"/media/"

try:
    from .settings_local import *
except ImportError as e:
    print(e)