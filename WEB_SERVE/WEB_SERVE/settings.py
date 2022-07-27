# -*- coding: utf-8 -*-

"""
Django settings for WEB_SERVE project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# ----------- START: Native Imports ---------- #
import os

from uuid import uuid4
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
from configurations import Configuration

from corsheaders.defaults import default_headers
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.utils import get_build_settings
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
    'DjangoConfigurations',
]


build_home = os.environ['BUILD_HOME']

build_settings = get_build_settings()

django_settings = build_settings['django-settings']

sqlite_settings = build_settings['sqlite']


class DjangoConfigurations(Configuration):

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
    #
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = django_settings.get('debug', False) or False

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = django_settings.get('secret_key') or uuid4().__str__()

    ALLOWED_HOSTS = ['*']

    CORS_ORIGIN_ALLOW_ALL = True

    CORS_ALLOW_HEADERS = list(default_headers) + ['workspace', 'Request-Id']

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ] + [
        #
        # All custom inclusions go here.

        'rest_framework',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ] + [
        #
        # All custom inclusions go here.
    ]

    ROOT_URLCONF = 'WEB_SERVE.urls'

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

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(build_home, 'data', sqlite_settings['database_name'])
        }
    }

    WSGI_APPLICATION = 'WEB_SERVE.wsgi.application'

    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    STATIC_URL = '/static/'
