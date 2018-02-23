from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Event, Schedule


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
            'fields': ('headline', 'text', ('date', 'recurring')),
        }),
        (_('Image Gallery'), {
            'fields': ('gallery',),
        }),
        (_('Main Link'), {
            'classes': ('collapse',),
            'fields': ('link_text', 'link', 'page'),
        }),
    )


plugin_pool.register_plugin(SchedulePlugin)
plugin_pool.register_plugin(EventPlugin)
