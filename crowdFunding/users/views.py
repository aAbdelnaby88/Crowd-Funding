from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth import  login , authenticate
from .forms import UserForm , ProfileForm
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def userProfile(request,id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get(user_name=id)
    context={'profile' : profile , 'user' : user}
    return render(request,"users/profile.html", context)

def index(request):
    return render(request,"users/test.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data.__ge__('username')
            password = form.changed_data.__ge__('password')

            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('registeration/login')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/signup.html', context)