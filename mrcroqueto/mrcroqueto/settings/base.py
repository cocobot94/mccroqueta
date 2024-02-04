"""
Django settings for mrcroqueto project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)tr&)c4@&8q8u$5qq0*uqtns(dp5^#6%%j*@nwnw356dy=t^uv"


# Application definition

BASE_APPS = [
    "apps.registration",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "apps.api",
    "apps.users",
    "apps.core",
    "apps.products",
    "apps.links",
    "apps.blog",
    "apps.news",
]
THIRD_APPS = [
    "storages",
    "import_export",
    "rest_framework",
    "ckeditor",
    "drf_yasg",
    "corsheaders",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "mrcroqueto.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.links.processors.ctx_links",
            ],
        },
    },
]

WSGI_APPLICATION = "mrcroqueto.wsgi.application"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "https://croqueto-3e4467808c40.herokuapp.com",
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = "users.User"


# Auth redirects
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


"""EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Your Email'
EMAIL_HOST_PASSWORD = 'Your Password'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False"""

# Importa el backend de almacenamiento
# from storages.backends.s3boto3 import S3Storage

AWS_ACCESS_KEY_ID = "AKIA2CFPTPDSJEQVBOHO"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "pruebacroqueto"
AWS_S3_SIGNATURE_NAME = ("s3v4",)
AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

"""AWS_S3_STATICFILES_LOCATION = "staticfiles"
AWS_S3_STATICFILES_STORAGE = "storages.backends.s3boto3.3Storage"

# Configuración para archivos multimedia (nueva clave staticfiles)
AWS_S3_MEDIA_LOCATION = "media"
AWS_S3_MEDIA_STORAGE = "storages.backends.s3boto3.3Storage"
"""
