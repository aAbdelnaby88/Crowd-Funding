# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name=("User Name"))
    email_confirmation = models.BooleanField(default=False , verbose_name=("Email"))
    phone_validation = RegexValidator(regex=r'^01[5|1|2|0][0-9]{8}$',
                                 message=" Please ,, Entered the Phone number in the format: '010|212|134|156'.")
    phone = models.CharField(max_length=11, null=True, blank=True , verbose_name=("Phone"))
    facebook =  models.URLField(null=True, blank=True , verbose_name=("FaceBook"))
    country = models.CharField(max_length=30, blank=True , verbose_name=("Country"))
    birth_date = models.DateField(null=True, blank=True, verbose_name=("BirthDate"))
    user_image = models.ImageField(upload_to='images/users/', default='images/default.jpg')

    def __str__(self):
        return str(self.user_name)


    def remove_image_update(self):
        pass

    def delete(self, *args, **kwargs):
        pass

    def update_user_profile(sender, instance, created, **kwargs):
        pass

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user_name=kwargs['instance'])


    post_save.connect(create_profile, sender=User)
