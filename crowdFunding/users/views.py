from django.shortcuts import render
from .models import Profile
# Create your views here.

def userProfile(request):
    return render(request,"users/profile.html")

def index(request):
    return render(request,"users/test.html")


