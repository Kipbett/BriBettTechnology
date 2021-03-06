# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-21 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BrianWeb', '0003_auto_20200221_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrianWeb.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='updateinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrianWeb.User'),
        ),
    ]
