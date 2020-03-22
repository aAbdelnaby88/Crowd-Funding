# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ProjectsForm
from django.http.response import HttpResponse

# Create your views here.

def create (request):
    if request.method == 'POST' :
        form = ProjectsForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return HttpResponse("Done ya boy")
        return HttpResponse("msh Done ya boy")
    else:

        form = ProjectsForm()
        context = {
            'form' : form ,
        }
        return render (request , 'projects/create.html' , context)
