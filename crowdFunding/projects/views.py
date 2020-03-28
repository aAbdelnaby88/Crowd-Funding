# -*- coding: utf-8 -*-
from .models import *
from django.shortcuts import render, redirect
from .forms import ProjectsForm
from django.http.response import HttpResponse
from users.models import Profile
from django.contrib.auth.models import User
# Create your views here.


def showProject(request, id):
    item = Project.objects.get(id=id)
    pPics = ProjectPicture.objects.all().filter(project_id=id)
    context = {'pData': item,
               'pPics': pPics}
    return render(request, "projects/viewProject.html", context)


def create(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user.profile
            new_form.save()
            return HttpResponse("Done ya boy")
        return HttpResponse("msh Done ya boy")
    else:

        form = ProjectsForm()
        context = {
            'form': form,
        }
    return render(request, 'projects/create.html', context)


def create_comment(request, id):
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST['content']
        comment.project_id = id
        comment.user = request.user.profile_set.first()
        comment.save()
        return redirect(f'/projects/{id}')
