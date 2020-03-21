# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# def __str__(self):
#     return self.phone
# Create your models here.
class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_confirmation = models.BooleanField(default=False)
    # phone_validation = RegexValidator(regex=r'^01[5|1|2|0][0-9]{8}$',
    #                              message=" Please ,, Entered the Phone number in the format: '010|212|134|156'.")
    phone = models.CharField(max_length=11, null=True, blank=True)
    facebook =  models.URLField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    #