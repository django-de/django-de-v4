from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from ..base import BasePlugin
from .models import TextContent


class TextPlugin(BasePlugin):
    name = _('Text')
    model = TextContent

    render_template = 'content/text/text.html'
    base_fields = BasePlugin.base_fields + ('headline', 'text')
    context_fields = BasePlugin.context_fields + ('headline', 'text')

plugin_pool.register_plugin(TextPlugin)
