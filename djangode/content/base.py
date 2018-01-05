from cms.plugin_base import CMSPluginBase as DjangoCMSPluginBase
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext


class BaseContent(models.Model):
    css_class = models.CharField(_('CSS Class'), max_length=64, blank=True)

    class Meta:
        abstract = True
        app_label = 'content'


class BasePlugin(DjangoCMSPluginBase):
    base_fields = ()
    advanced_fields = ('css_class',)
    context_fields = ('css_class',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {
                'fields': self.base_fields
            }),
            (ugettext('Advanced options'), {
                'classes': ('collapse',),
                'fields': self.advanced_fields
            })
        ]
        return fieldsets

    def render(self, context, instance, placeholder):
        context = super(BasePlugin, self).render(context, instance, placeholder)

        context['content_id'] = instance.pk
        context.update(dict((key, getattr(instance, key)) for key in self.context_fields))

        return context
