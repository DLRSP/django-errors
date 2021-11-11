"""Test's settings"""
DEBUG = False

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

SECRET_KEY = "NOTASECRET"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = ["django_errors"]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates"}]

ROOT_URLCONF = "tests.urls"

USE_TZ = True
