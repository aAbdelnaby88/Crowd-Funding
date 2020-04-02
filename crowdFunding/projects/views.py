from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectsForm, ImageForm
from django.http.response import HttpResponse, JsonResponse
from users.models import Profile
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
# Create your views here.
from taggit.models import Tag
from django.db.models import Avg
from decimal import Decimal, ROUND_HALF_UP

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def showProject(request, id):
    item = Project.objects.get(id=id)
    pPics = ProjectPicture.objects.all().filter(project_id=id)
    rate = item.rate_set.all().aggregate(Avg("value"))["value__avg"]
    print(rate)
    rate = rate if rate else 0
    rate = Decimal(rate).quantize(0, ROUND_HALF_UP)
    
    context = {'pData': item,
               'pPics': pPics,
               'rate': rate}
    if request.user:
        user_rate = item.rate_set.filter(
            user_id=request.user.profile.id).first()
        print(user_rate)
        if user_rate:
            context["user_rate"] = user_rate.value
    return render(request, "projects/viewProject.html", context)


def showCategoryProjects(request, id):
    category = Category.objects.get(id=id)
    context = {'catName': category}
    return render(request, "projects/viewCategory.html", context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def create(request):

    ImageFormSet = modelformset_factory(
        ProjectPicture, form=ImageForm, min_num=1, extra=3)

    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=ProjectPicture.objects.none())

        if form.is_valid() and formset.is_valid():
            new_form = form.save(commit=False)
            new_form.user = Profile.objects.get(user=request.user)
            new_form.save()
            form.save_m2m()
            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['img_url']
                    photo = ProjectPicture(project=new_form, img_url=image)
                    photo.save()
            return redirect(f'/projects/projectDetails/{new_form.id}')
        context = {
            'form': form,
            'formset': formset,
        }
        return render(request, 'projects/create.html', context)
    else:

        form = ProjectsForm()
        formset = ImageFormSet(queryset=ProjectPicture.objects.none())
        context = {
            'form': form,
            'formset': formset,
        }
    return render(request, 'projects/create.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_comment(request, id):
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST['content']
        comment.project_id = id
        comment.user = request.user.profile
        comment.save()
        return redirect(f'/projects/projectDetails/{id}')


def home(request):
    lFiveList = Project.objects.extra(order_by=['created_at'])
    categories = Category.objects.all()
    featuredList = Project.objects.all().filter(is_featured='True')
    context = {
        'latestFiveList': lFiveList,
        'categs': categories,
        'fProject': featuredList,
    }
    return render(request, 'projects/Home.html', context)


def show_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)

    projects = Project.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'projects': projects,
    }
    return render(request, 'projects/tag.html', context)


def report_project(request, id):
    if request.method == 'POST':
        report_pro = ProjectReport.objects.create(
            content=request.POST['report'],
            project_id=id,
            user=request.user.profile
        )
        # report_pro.content += request.POST['content']
        # report_pro.project_id = id
        # report_pro.user = request.user.profile
        # report_pro.save()
        return redirect(f'/projects/projectDetails/{id}')


def report_comment(request, id):
    if request.method == 'POST':
        if len(list(CommentReport.objects.filter(comment_id=request.POST['comment_id'], user=request.user.profile))) == 0:
            report_com = CommentReport.objects.create(

                comment_id=request.POST['comment_id'],
                user=request.user.profile
            )
        else:
            messages.error(request, 'You reported this comment before!')
        return redirect(f'/projects/projectDetails/{id}')


@login_required
def rate_project(request, id, value):
    if request.method == 'POST':
        user_id = request.user.profile.id
        print(f"{user_id} {id} {value}")

        Rate.objects.update_or_create(
            project_id=id,
            user_id=user_id,
            defaults={"value": value},
        )
        data = {
            'msg': "success"
        }
        return JsonResponse(data)
