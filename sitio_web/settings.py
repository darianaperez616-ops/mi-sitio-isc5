from pathlib import Path
import os
import pymysql
pymysql.install_as_MySQLdb()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^2$&3kpna1j#5bujuo$@(text#r-0^#094p1(^t#(v2p#&+3w^'

# 🔹 Modo debug automático:
DEBUG = "False"

ALLOWED_HOSTS = [
    ".elasticbeanstalk.com",
    ".amazonaws.com",
    "localhost",
    "127.0.0.1",
    ["*"]
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'rest_framework',  # ← NECESARIO para tus ViewSets
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ← OBLIGATORIO
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ROOT_URLCONF = 'sitio_web.urls'

# 🔹 Plantillas (templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ← Asegúrate de que esté así
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


WSGI_APPLICATION = 'sitio_web.wsgi.application'



# 🔹 Base de datos (automática local ↔ AWS)
if os.getenv("RDS_HOSTNAME"):
    # PRODUCCIÓN (AWS RDS)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('RDS_DB_NAME'),
            'USER': os.getenv('RDS_USERNAME'),
            'PASSWORD': os.getenv('RDS_PASSWORD'),
            'HOST': os.getenv('RDS_HOSTNAME'),
            'PORT': os.getenv('RDS_PORT', '3306'),
        }
    }
else:
    # LOCAL (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# 🔹 Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]  # ← si tienes carpeta static local

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
