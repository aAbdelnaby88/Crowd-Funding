from .models import *
from django.shortcuts import render , redirect
from .forms import ProjectsForm , ImageForm
from django.http.response import HttpResponse
from users.models import Profile
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from .models import ProjectPicture , Project
from django.contrib import messages

# Create your views here.


def showProject(request, id):
    item = Project.objects.get(id=id)
    pPics = ProjectPicture.objects.all().filter(project_id=id)
    context = {'pData': item,
               'pPics': pPics}
    return render(request, "projects/viewProject.html", context)


def showCategoryProjects(request , id):
    category=Category.objects.get(id=id)
    context = { 'catName' : category  }
    return render(request,"projects/viewCategory.html", context)


def create (request):

    ImageFormSet = modelformset_factory(ProjectPicture,form=ImageForm , extra=1 )
                                        
    if request.method == 'POST' :
        form = ProjectsForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            new_form = form.save(commit=False)
            new_form.user = Profile.objects.get(user_name=request.user)
            new_form.save()
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['img_url']
                    photo = ProjectPicture(project=new_form, img_url=image)
                    photo.save()
            return HttpResponse("Done ya boy")
        return HttpResponse("msh Done ya boy")
    else:

        form = ProjectsForm()
        formset = ImageFormSet()
        context = {
            'form' : form ,
            'formset' : formset ,
        }
    return render(request, 'projects/create.html', context)


def create_comment(request, id):
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST['content']
        comment.project_id = id
        comment.user = request.user.profile_set.first()
        comment.save()
        return redirect(f'/projects/projectDetails/{id}')

def home (request):
    lFiveList= Project.objects.extra(order_by=['insert_date'])
    categories= Category.objects.all()
    featuredList= Project.objects.all().filter(is_featured='True')
    context = {
        'latestFiveList': lFiveList,
        'categs': categories,
        'fProject': featuredList,
    }
    return render(request,'projects/Home.html',context)