from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Image


class ImagePlugin(CMSPluginBase):
    name = _('Image')
    model = Image
    render_template = 'images/image/large.html'

    def _get_render_template(self, context, instance, placeholder):
        return 'images/image/{0}'.format(instance.template)


plugin_pool.register_plugin(ImagePlugin)
