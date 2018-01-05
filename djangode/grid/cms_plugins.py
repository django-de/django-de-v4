from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Grid, Tile


class GridPlugin(CMSPluginBase):
    name = _('Info Grid')
    model = Grid
    render_template = 'grid/grid.html'
    allow_children = True
    child_classes = ('GridTilePlugin',)
    fieldsets = (
        (None, {
            'fields': ('headline',)
        }),
        ('Main Link', {
            'classes': ('collapse',),
            'fields': ('link_text', 'link', 'page'),
        }),
    )


class GridTilePlugin(CMSPluginBase):
    name = _('Tile')
    model = Tile
    render_template = 'grid/tile.html'
    require_parent = True
    fieldsets = (
        (None, {
            'fields': ('headline', 'image')
        }),
        ('Main Link', {
            'classes': ('collapse',),
            'fields': ('link_text', 'link', 'page'),
        }),
    )


plugin_pool.register_plugin(GridPlugin)
plugin_pool.register_plugin(GridTilePlugin)
