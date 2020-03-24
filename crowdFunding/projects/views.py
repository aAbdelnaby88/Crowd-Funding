# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *
from django.shortcuts import render

# Create your views here.

def showProject(request , id):
    item = Project.objects.get(id=id)
    pPics= ProjectPicture.objects.all().filter(project_id=id)
    context = { 'pData' : item ,
            'pPics' : pPics}
    return render(request,"projects/viewProject.html", context)