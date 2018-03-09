import os
import dj_database_url
from djangode.conf.global_settings import *

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

MANAGERS = ADMINS = (
    ('Django e.V.', os.environ.get('ADMIN_EMAIL')),
)

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SECRET_KEY = os.environ.get('SECRET_KEY', '')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

MEDIA_ROOT = os.environ.get('MEDIA_ROOT')
STATIC_ROOT = os.environ.get('STATIC_ROOT')
MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'

# Sentry
INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
RAVEN_CONFIG = {'dsn': os.environ.get('RAVEN_DSN', None)}
