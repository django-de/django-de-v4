from cms.plugin_base import CMSPluginBase


class MDEPluginBase(CMSPluginBase):
    """
    CMSPlugin that automatically enables the SimpleMDE markdown editor
    on all `textarea` fields.
    """
    change_form_template = 'admin/mde_change_form.html'

    class Media:
        js = ['https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js']
        css = {
            'all': ['https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css']
        }

