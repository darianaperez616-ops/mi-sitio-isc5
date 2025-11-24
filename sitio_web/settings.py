from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-temporal-123456789'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = ['django.contrib.staticfiles']
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']

ROOT_URLCONF = 'sitio_web.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
}]

WSGI_APPLICATION = 'sitio_web.wsgi.application'

DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3')}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
