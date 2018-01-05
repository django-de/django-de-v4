import os
import uuid

from django.utils.translation import ugettext_lazy as _


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

    'djangode.content.apps.ContentConfig',
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

MIDDLEWARE_CLASSES = (
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
)

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

CACHE_MIDDLEWARE_SECONDS = 60

LOGGING = {
    'version': 1,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'djangode': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'django': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
    }
}

CMS_TEMPLATES = [
    ('cms.html', _('Default template'))
]

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

CMS_ENABLE_UPDATE_CHECK = False
