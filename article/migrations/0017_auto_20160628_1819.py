# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20160628_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_only',
            new_name='written_only',
        ),
    ]