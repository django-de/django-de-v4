from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page

from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

ICON_HELP = 'Icon name from http://thesabbir.github.io/simple-line-icons/ ' \
    'e.g. "paper-clip"'

#==============================================================================
# Homepage
#==============================================================================


class WeDoBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    image = ImageChooserBlock(required=True)
    link = blocks.CharBlock(required=False)


class DocumentsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    document = DocumentChooserBlock(required=True)


class HomePage(Page):
    teaser = RichTextField('Teaser')

    what_is_title = models.CharField('What is - Title', max_length=100)
    what_is_desc = RichTextField('What is - Description')

    we_are_title = models.CharField('We are - Title', max_length=100)
    we_are_desc = RichTextField('We are - Description')
    we_are_files = StreamField([
        ('doc', DocumentsBlock()),
    ], blank=True, verbose_name='Documents')

    we_help_title = models.CharField('Where we help title', max_length=100)
    we_help_items = StreamField([
        ('item', WeDoBlock()),
    ], blank=True, verbose_name='Where we help Items')

    # --- Wagtail Settings ----------------------------------------------------
    template = 'homepage.html'
    content_panels = Page.content_panels + [
        FieldPanel('teaser'),

        FieldPanel('what_is_title'),
        FieldPanel('what_is_desc'),

        FieldPanel('we_are_title'),
        FieldPanel('we_are_desc'),
        StreamFieldPanel('we_are_files'),

        FieldPanel('we_help_title'),
        StreamFieldPanel('we_help_items'),
    ]

#==============================================================================
# ContentPage
#==============================================================================


class SectionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(required=False)


class ContentPage(Page):
    description = RichTextField(blank=True, null=True)
    sections = StreamField([
        ('item', SectionBlock()),
    ], blank=True, verbose_name='Section')

    # --- Wagtail Settings ----------------------------------------------------
    template = 'page.html'
    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        StreamFieldPanel('sections'),
    ]


#==============================================================================
# Events
#==============================================================================

class EventsPage(Page):
    description = RichTextField()

    # --- Wagtail Settings ----------------------------------------------------
    template = 'events.html'
    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    def events(self, recurring=False):
        return (Event.objects.live().descendant_of(self)
            .filter(recurring=recurring).order_by('-date'))

    def recurring(self):
        return self.events(recurring=True)

    def upcoming(self):
        return self.events().filter(date__gt=now())

    def recent(self):
        return self.events().filter(date__lte=now())


class Event(Page):
    description = RichTextField(blank=True, null=True)
    external_url = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    recurring = models.BooleanField(default=False)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Main Image',
    )
    images = StreamField([
        ('image', ImageChooserBlock()),
    ], blank=True, verbose_name='Gallery Images')
    credit = RichTextField('Image Credit', blank=True, null=True)

    # --- Wagtail Settings ----------------------------------------------------
    template = 'event.html'
    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('external_url'),
        FieldPanel('date'),
        FieldPanel('recurring'),
        ImageChooserPanel('image'),
        StreamFieldPanel('images'),
        FieldPanel('credit'),
    ]

#==============================================================================
# Help
#==============================================================================

class HelpItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=False)
    link = blocks.URLBlock(required=False)


class HelpPage(Page):
    description = RichTextField()
    items = StreamField([
        ('item', HelpItemBlock()),
    ], blank=True)

    # --- Wagtail Settings ----------------------------------------------------
    template = 'help.html'
    content_panels =Page.content_panels + [
        FieldPanel('description', classname="full"),
        StreamFieldPanel('items'),
    ]

#==============================================================================
# Help
#==============================================================================

@register_snippet
@python_2_unicode_compatible
class TextSnippet(models.Model):
    text = models.CharField(max_length=255)
    panels = [FieldPanel('text'),]

    def __str__(self):
        return self.text
