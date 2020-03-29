from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth import  login , authenticate
from .forms import SignUpForm
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('registeration/login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)




