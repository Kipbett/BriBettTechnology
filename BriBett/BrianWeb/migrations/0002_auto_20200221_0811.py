# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-21 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BrianWeb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_descrption',
            new_name='project_description',
        ),
    ]
