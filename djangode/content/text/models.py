from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..base import BaseContent


class TextContent(CMSPlugin, BaseContent):
    headline = models.CharField(_('Headline'), max_length=255, blank=True)
    text = models.TextField(_('Text'), blank=True)

    def __str__(self):
        if self.headline:
            return '<{0}>'.format(self.headline)
        return '<{0}>'.format(self.text[:23])
