from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import TextContent, TeaserContent


class TextPlugin(CMSPluginBase):
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


class TeaserPlugin(CMSPluginBase):
    name = _('Teaser')
    model = TeaserContent
    render_template = 'content/teaser.html'


plugin_pool.register_plugin(TextPlugin)
plugin_pool.register_plugin(TeaserPlugin)
