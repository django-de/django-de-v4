"""
HEROKU specific settings
"""
from .base import *   # pylint: disable=W0614,W0401
import os
import dj_database_url

ALLOWED_HOSTS = ('*',)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', None)

DEBUG = os.environ.get('DJANGO_DEBUG', False) == "True"  # Set env var to "True"

ADMINS = (
    ('Django e.V.', os.getenv('DJANGO_ADMIN_EMAIL')),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(),
}
