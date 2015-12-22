"""
WSGI config for djde project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

# os.environ["DJANGO_SETTINGS_MODULE"] IS REQUIRED

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(get_wsgi_application())
