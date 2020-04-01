# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from users.models import Profile
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

class Project(models.Model):
    title = models.CharField(max_length=45)
    details = models.TextField(max_length=3000)
    target = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)

class Category(models.Model):
    name = models.CharField(max_length=45)
    cat_icon = models.ImageField(upload_to='static/imgs/', default=True)
    def __str__(self):
        return str(self.name)


class ProjectPicture(models.Model):
    img_url = models.ImageField(upload_to = 'imgs/' ,verbose_name='Image')
    project = models.ForeignKey(Project, on_delete=models.CASCADE , default=None)

    def __str__(self):
        return str(self.project.title)


class Comment(models.Model):
    content = models.TextField(max_length=3000, blank=False, default=None)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f'comment by {self.user.user_name.username} on {self.project.title} project.')


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

    created_at = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    value = models.IntegerField()
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

