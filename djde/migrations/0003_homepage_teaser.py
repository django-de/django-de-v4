# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 16:30
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djde', '0002_event_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='teaser',
            field=wagtail.wagtailcore.fields.RichTextField(default='', verbose_name='Teaser'),
            preserve_default=False,
        ),
    ]