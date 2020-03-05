# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name

class Projects(models.Model):
    project_id = models.CharField(max_length=100, unique=True)
    project_title = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='projects')
    project_description = models.TextField(max_length=2500)

    def __str__(self):
        return self.project_title

class UpdateInfo(models.Model):
    project_id = models.ForeignKey(Projects, on_delete= models.CASCADE)
    date_modified = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_id)

