# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-18 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwward', '0002_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='user',
            new_name='poster',
        ),
    ]
