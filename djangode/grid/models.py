from __future__ import unicode_literals

from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Grid(CMSPlugin):
    headline = models.CharField(_('Headline'), max_length=4000, blank=True)
    link = models.CharField(_('Link'), blank=True, max_length=4000)
    page = PageField(
        verbose_name=('CMS Page'), blank=True, null=True,
        help_text=_('If both link and cms page is defined, the link is preferred.'))
    link_text = models.CharField(_('Link Text'), blank=True, max_length=4000)

    def __str__(self):
        return '{0}'.format(self.headline[:23])


@python_2_unicode_compatible
class Tile(CMSPlugin):
    headline = models.CharField(_('Headline'), max_length=4000, blank=True)
    image = FilerImageField(verbose_name=_('Main Image'), null=True, blank=True)
    link = models.CharField(_('Link'), blank=True, max_length=4000)
    page = PageField(
        verbose_name=('CMS Page'), blank=True, null=True,
        help_text=_('If both link and cms page is defined, the link is preferred.'))
    link_text = models.CharField(_('Link Text'), blank=True, max_length=4000)

    def __str__(self):
        return '{0}'.format(self.headline[:23])

