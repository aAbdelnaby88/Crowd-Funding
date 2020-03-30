from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth import  login , authenticate
from .forms import SignUpForm , UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



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


@login_required
def userProfile(request, uid):
    user2 = get_object_or_404(User, id=uid)
    # categories = Categories.objects.all()

    # if request.user.id == user2.id:
    context = {
            'userprofile': user2,

    }

    return render(request,"users/profile.html", context)


@login_required
def editProfile(request, uid):
    user2 = get_object_or_404(User, id=uid)
    # categories = Categories.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile', uid=uid)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "userprofile": user2,
        # "categories": categories,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "users/edit_profile.html", context)