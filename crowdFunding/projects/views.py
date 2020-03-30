from .models import *
from django.shortcuts import render
from .forms import ProjectsForm
from django.http.response import HttpResponse
from users.models import Profile
from django.contrib.auth.models import User
# Create your views here.


def showProject(request , id):
    item = Project.objects.get(id=id)
    pPics= ProjectPicture.objects.all().filter(project_id=id)
    context = { 'pData' : item ,
            'pPics' : pPics}
    return render(request,"projects/viewProject.html", context)


def showCategoryProjects(request , id):
    category=Category.objects.get(id=id)
    projectsList=Project.objects.all().filter(category_id=id)
    projectImg = ProjectPicture.objects.none()

    for p in projectsList:
        projectImg = ProjectPicture.objects.distinct().order_by('project_id')
        
    context = { 'catName' : category ,
            'projData' : projectsList,
            'projImgs':projectImg }
    return render(request,"projects/viewCategory.html", context)


def create (request):
    if request.method == 'POST' :
        form = ProjectsForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user.profile
            new_form.save()
            return HttpResponse("Done ya boy")
        return HttpResponse("msh Done ya boy")
    else:

        form = ProjectsForm()
        context = {
            'form' : form ,
        }
        return render (request , 'projects/create.html' , context)

