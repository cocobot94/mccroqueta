from .base import *

# import django_heroku
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [
    "croqueto-3e4467808c40.herokuapp.com",
    "http://www.mccroqueta.com/",
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

import dj_database_url

# Configuración de la base de datos para Heroku Postgres
DATABASES = {"default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))}

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "..//apps/core/static"),)

