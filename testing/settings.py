import logging
import os
import tempfile

from djangode.conf.global_settings import *


RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')
SECRET_KEY = 'testing'

if os.environ.get('CI', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': 'postgres',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'djangode_test',
        }
    }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'djangode_test',
    }
}

MEDIA_ROOT = tempfile.mkdtemp()
STATIC_ROOT = tempfile.mkdtemp()

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)

logging.disable(logging.CRITICAL)
