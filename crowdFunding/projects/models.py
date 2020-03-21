# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from users.models import User
# Create your models here.


class Project(models.Model):
    title = models.TextField(max_length=45)
    details = models.TextField(max_length=3000)
    target = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rate = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    rates_count = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")


class Category(models.Model):
    name = models.TextField(max_length=45)


class ProjectPicture(models.Model):
    img_url = models.URLField()
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.TextField(max_length=45)


class Comment(models.Model):
    content = models.TextField(max_length=3000)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)


class ProjectReport(models.Model):
    content = models.TextField(max_length=3000)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)


class CommentReport(models.Model):
    content = models.TextField(max_length=3000)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)


class Donation(models.Model):
    amount = models.IntegerField()
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
