import os
import uuid
import logging.config

from django.utils.translation import ugettext_lazy as _
from django.utils.log import DEFAULT_LOGGING

DEBUG = False

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(PROJECT_DIR)

ROOT_URLCONF = 'djangode.urls'
WSGI_APPLICATION = 'djangode.wsgi.application'

SECRET_KEY = str(uuid.uuid4().hex)
ALLOWED_HOSTS = []

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'django-de-website@localhost'
EMAIL_SUBJECT_PREFIX = os.path.basename(PROJECT_DIR)

LANGUAGES = [
    ('de', _('German')),
]
LANGUAGE_CODE = 'de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

USE_ETAGS = True

SITE_ID = 1

SESSION_COOKIE_SECURE = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = (
    'djangocms_admin_style',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'filer',
    'easy_thumbnails',
    'django_markup',

    'djangode',
    'djangode.content',
    'djangode.schedule',
    'djangode.grid',
    'djangode.images',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(ROOT_DIR, 'templates')],
        'OPTIONS': {
            'debug': False,
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

MEDIA_ROOT = os.path.join(ROOT_DIR, 'web', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT_DIR, 'web', 'static')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, '..', 'build'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'djangode_dev',
    }
}

CACHE_MIDDLEWARE_SECONDS = 3600

CMS_CACHE_DURATIONS = {
    'content': CACHE_MIDDLEWARE_SECONDS,
    'menus': CACHE_MIDDLEWARE_SECONDS,
    'permissions': 0,
}

# ==============================================================================
# CMS
# ==============================================================================

THUMBNAIL_HIGH_RESOLUTION = False

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

CMS_TEMPLATES = [
    ('default.html', _('Default template'))
]

CMS_TEMPLATE_INHERITANCE = False

CMS_TOOLBARS = [
    'cms.cms_toolbars.PlaceholderToolbar',
    'cms.cms_toolbars.BasicToolbar',
    'cms.cms_toolbars.PageToolbar',
]

CMS_PLACEHOLDER_CONF = {
    'main': {
        'name': _('Main content'),
    },
}

CMS_ENABLE_UPDATE_CHECK = True


# ==============================================================================
# Logging
# ==============================================================================

# Default JS Log Level (error, info, trace, ...)
JS_LOG_LEVEL = os.getenv('JS_LOG_LEVEL', 'error')

# Default Python Log Level (error, warning, info, debug, ...)
PY_LOG_LEVEL = os.environ.get('LOG_LEVEL', 'warning').upper()

# Disable Django's logging setup
LOGGING_CONFIG = None
LOGGING_DICT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'simple': {'format': '%(levelname)s %(message)s'},
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        # Add Handler for Sentry for `warning` and above
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': PY_LOG_LEVEL,
            'handlers': ['console', 'sentry'],
        },

        # Our application code
        'djangode': {'level': PY_LOG_LEVEL, 'handlers': ['console', 'sentry'], 'propagate': False},

        # Prevent noisy modules from logging to Sentry
        # 'noisy_module': {
        #     'level': 'ERROR',
        #     'handlers': ['console'],
        #     'propagate': False,
        # },

        # Default runserver request logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],

        # Force INFO logging for common django loggers
        # so LOG_LEVEL=DEBUG would not apply to them.
        'django.requests': {'level': 'WARNING', 'handlers': ['console', 'sentry'], 'propagate': False},
        'django.template': {'level': 'WARNING', 'handlers': ['console', 'sentry'], 'propagate': False},
        'django.db': {'level': 'WARNING', 'handlers': ['console', 'sentry'], 'propagate': False},

        # Disable `RemovedInDjango110Warning` warnings
        'py.warnings': {'level': 'ERROR', 'handlers': ['console']},
    },
}

# Apply logging dict config
logging.config.dictConfig(LOGGING_DICT)
