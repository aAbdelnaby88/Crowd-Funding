from django.http import HttpResponse
from django.shortcuts import render
from users.models import Profile
from django.contrib.auth.models import User
# Create your views here.

def userProfile(request,id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get(user_name=id)
    context={'profile' : profile , 'user' : user}
    return render(request,"users/profile.html", context)

def index(request):
    return render(request,"users/login.html")

