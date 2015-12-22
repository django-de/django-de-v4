"""
HEROKU specific settings
"""
from .base import *   # pylint: disable=W0614,W0401
import os
import dj_database_url

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', None)

DEBUG = os.environ.get('DJANGO_DEBUG', False) == "True"  # Set env var to "True"

ADMINS = (
    ('Django e.V.', os.environ.get('DJANGO_ADMIN_EMAIL')),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(),
}

#==============================================================================
# Store media uploads on S3
#==============================================================================

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

INSTALLED_APPS += ('storages',)

# Use Amazon S3 for storage for uploaded media files.
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Amazon S3 settings.
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_AUTO_CREATE_BUCKET = False
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = True
AWS_REDUCED_REDUNDANCY = False
AWS_IS_GZIPPED = False

MEDIA_ROOT = '/'
MEDIA_URL = '//s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
