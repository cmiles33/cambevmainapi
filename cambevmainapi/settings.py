"""
Django settings for cambevmainapi project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-awofi&)het2l#hj0ea(ck*o$@xm7@nreq^sa51(p!47o1l&)sm'

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
    'corsheaders',
    'djoser',
    'storages',

    'ceramicstore.apps.CeramicstoreConfig',


]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cambevmainapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'cambevmainapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

S3_used_bool = False

if S3_used_bool:
    SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'root')
    COMPRESS_ROOT = os.path.join(BASE_DIR, 'root')
    AWS_ACCESS_KEY_ID = 'AKIATYDJEXKYD7Y65T62'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'ccmbtesting7651f021-37ee-498b-b019-22c1963785d0'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = None
    AWS_LOCATION = 'static'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'boot'),
        os.path.join(BASE_DIR,'root')
    ]

    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    DEFAULT_FILE_STORAGE = 'cambevmainapi.storage_backends.MediaStorage'
else:
    COMPRESS_ROOT = os.path.join(BASE_DIR, 'root')
    STATIC_URL = 'root/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'root')
    # Sass Root
    SASS_PROCESSOR_ROOT = STATIC_ROOT
    # AWS STUFF FOR MEDIA FILES

    AWS_ACCESS_KEY_ID = 'AKIATYDJEXKYD7Y65T62'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'ccmbtesting7651f021-37ee-498b-b019-22c1963785d0'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = None

    DEFAULT_FILE_STORAGE = 'cambevmainapi.storage_backends.MediaStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'