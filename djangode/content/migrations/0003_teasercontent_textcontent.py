# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-05 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('content', '0002_auto_20180105_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeaserContent',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_teasercontent', serialize=False, to='cms.CMSPlugin')),
                ('teaser', models.TextField(blank=True, verbose_name='Headline')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_textcontent', serialize=False, to='cms.CMSPlugin')),
                ('headline', models.CharField(blank=True, max_length=4000, verbose_name='Headline')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
                ('link', models.CharField(blank=True, max_length=4000, verbose_name='Link')),
                ('alignment', models.CharField(choices=[(b'top', 'Top'), (b'left', 'Left')], default=b'top', max_length=10, verbose_name='Title Alignment')),
                ('theme', models.CharField(choices=[(b'teaser', 'Teaser'), (b'white', 'White'), (b'alternate', 'Alternate')], default=b'white', max_length=10, verbose_name='Background Theme')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]