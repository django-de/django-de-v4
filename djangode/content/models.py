from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from django.template.defaultfilters import striptags
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class PlainTextContent(CMSPlugin):
    text = models.TextField(_('Text'), blank=True)
    html = models.BooleanField(_('Allow HTML'), default=False)

    def __str__(self):
        return '{0}'.format(striptags(self.text[:23]))


@python_2_unicode_compatible
class TextContent(CMSPlugin):
    ALIGNMENT_CHOICES = (
        ('top', _('Top')),
        ('left', _('Left')),
    )
    BACKGROUND_CHOICES = (
        ('page-title', _('Page Title')),
        ('regular', _('Regular (White)')),
        ('secondary', _('Secondary (Grey)')),
    )

    headline = models.CharField(_('Headline'), max_length=4000, blank=True)
    text = models.TextField(_('Text'), blank=True)
    link = models.CharField(_('Link'), blank=True, max_length=4000)
    page = PageField(
        verbose_name=('CMS Page'), blank=True, null=True,
        help_text=_('If both link and cms page is defined, the link is preferred.'))
    link_text = models.CharField(_('Link Text'), blank=True, max_length=4000)
    alignment = models.CharField(
        _('Title Alignment'), max_length=10,
        choices=ALIGNMENT_CHOICES,  default=ALIGNMENT_CHOICES[0][0])
    theme = models.CharField(
        _('Background Theme'), max_length=10,
        choices=BACKGROUND_CHOICES,  default=BACKGROUND_CHOICES[1][0])

    def __str__(self):
        if self.headline:
            return '<{0}>'.format(self.headline)
        return '{0}'.format(self.text[:23])


@python_2_unicode_compatible
class TeaserContent(CMSPlugin):
    teaser = models.TextField(_('Teaser'), blank=True)

    def __str__(self):
        return '{0}'.format(self.teaser[:23])
