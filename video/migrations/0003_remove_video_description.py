# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20160728_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
    ]