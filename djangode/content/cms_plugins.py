from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from ..cms_plugins import MDEPluginBase
from .models import TextContent, TeaserContent, PlainTextContent


class TextPlugin(MDEPluginBase):
    name = _('Title + Text')
    model = TextContent
    fieldsets = (
        (None, {
            'fields': ('headline', 'text', 'alignment', 'theme')
        }),
        ('Main Link', {
            'classes': ('collapse',),
            'fields': ('link_text', 'link', 'page'),
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        return 'content/text_{0}.html'.format(instance.alignment)


class TeaserPlugin(MDEPluginBase):
    name = _('Teaser')
    model = TeaserContent
    render_template = 'content/teaser.html'


class PlainTextPlugin(CMSPluginBase):
    name = _('Plain Text (no Layout)')
    model = PlainTextContent
    render_template = 'content/plain_text.html'


plugin_pool.register_plugin(TextPlugin)
plugin_pool.register_plugin(TeaserPlugin)
plugin_pool.register_plugin(PlainTextPlugin)
