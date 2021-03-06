# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20160628_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-article_date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='article',
            name='article_only',
            field=models.BooleanField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='video_only',
            field=models.BooleanField(default=''),
        ),
    ]
