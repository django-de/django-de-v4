from django import template
from django.utils.safestring import mark_safe

from wagtail.wagtailcore.models import Page


register = template.Library()

@register.assignment_tag(takes_context=True)
def get_page_tree(context, unpublished=False):
    root = context['request'].site.root_page
    return root.get_annotated_list()

@register.assignment_tag(takes_context=True)
def get_root_pages(context, unpublished=False):
    root = context['request'].site.root_page
    return root.get_children().live().public()
