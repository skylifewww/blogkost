# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20160612_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=250, verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_video',
            field=embed_video.fields.EmbedVideoField(blank=True, help_text='URL video', null=True, verbose_name='Видео'),
        ),
    ]
