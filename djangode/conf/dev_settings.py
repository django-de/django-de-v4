from djangode.conf.global_settings import *


SECRET_KEY = 'dev'
ALLOWED_HOSTS = ['localhost']

DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATES[0]['OPTIONS']['debug'] = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangode_dev',
    }
}

TEMPLATES[0]['OPTIONS']['loaders'] = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'djangode_dev',
    }
}

CACHE_MIDDLEWARE_SECONDS = 0

CMS_PAGE_CACHE = False
CMS_PLACEHOLDER_CACHE = False
CMS_PLUGIN_CACHE = False
