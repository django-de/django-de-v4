from __future__ import unicode_literals

from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from filer.fields.folder import FilerFolderField
from filer.models import Image


@python_2_unicode_compatible
class Schedule(CMSPlugin):
    headline = models.CharField(_('Headline'), max_length=4000, blank=True)

    def __str__(self):
        return '{0}'.format(self.headline[:23])


@python_2_unicode_compatible
class Event(CMSPlugin):
    headline = models.CharField(_('Headline'), max_length=4000, blank=True)
    text = models.TextField(_('Text'), blank=True)
    date = models.DateField(_('Date'), blank=True, null=True)
    recurring = models.BooleanField(_('Recurring'), default=False)
    link = models.CharField(_('Link'), blank=True, max_length=4000)
    page = PageField(
        verbose_name=('CMS Page'), blank=True, null=True,
        help_text=_('If both link and cms page is defined, the link is preferred.'))
    link_text = models.CharField(_('Link Text'), blank=True, max_length=4000)
    gallery = FilerFolderField(
        verbose_name=('Image Gallery'), blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.headline[:23])

    @property
    def gallery_images(self):
        if not self.gallery:
            return []
        return Image.objects.filter(folder=self.gallery)
