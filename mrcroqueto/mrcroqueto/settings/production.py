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

"""DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
}
}"""

"""DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d7i3340qqkik0p",
        "PASSWORD": "44303b6cd978c82fd206bd6874309a48abd66cdaf3d52b0acd7e23fd0098a005",
        "USER": "oxmqtxmmgpafld",
        "HOST": "ec2-3-232-218-211.compute-1.amazonaws.com",
        "PORT": "5432",
    }
}"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "..//apps/core/static"),)

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# django_heroku.settings(locals())
