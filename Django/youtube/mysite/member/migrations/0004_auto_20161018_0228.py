# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 02:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20161018_0205'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='youtubeuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='youtubeuser',
            name='username',
        ),
    ]