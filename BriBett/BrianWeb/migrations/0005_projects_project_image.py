# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-25 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BrianWeb', '0004_auto_20200221_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='projects'),
            preserve_default=False,
        ),
    ]