from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Image(CMSPlugin):
    IMAGE_TEMPLATES = [
        ('fullwidth.html', 'Full Width'),
        ('large.html', 'Large'),
        ('medium.html', 'Medium'),
    ]
    image = FilerImageField(verbose_name=_('Main Image'), null=True, blank=True)
    template = models.CharField(_('Template'), choices=IMAGE_TEMPLATES,
                                max_length=500)

    def __str__(self):
        return '{0}'.format(self.image)

