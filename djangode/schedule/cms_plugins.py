from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Schedule, Event, EventImage

class SchedulePlugin(CMSPluginBase):
    name = _('Schedule')
    model = Schedule
    render_template = 'schedule/schedule.html'
    allow_children = True
    child_classes = ('EventPlugin',)


class EventPlugin(CMSPluginBase):
    name = _('Event')
    model = Event
    render_template = 'schedule/event.html'
    require_parent = True
    allow_children = True
    child_classes = ('EventImagePlugin',)
    fieldsets = (
        (None, {
            'fields': ('headline',),
        }),
        ('Main Link', {
            'classes': ('collapse',),
            'fields': ('link_text', 'link', 'page'),
        }),
    )


class EventImagePlugin(CMSPluginBase):
    name = _('Image')
    model = EventImage
    render_template = 'schedule/image.html'
    require_parent = True


plugin_pool.register_plugin(SchedulePlugin)
plugin_pool.register_plugin(EventPlugin)
plugin_pool.register_plugin(EventImagePlugin)
