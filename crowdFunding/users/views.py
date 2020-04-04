from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, UserDeleteForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Avg, Sum
from django.contrib.auth.decorators import login_required
from users.models import Profile
from projects.models import Project, Category, Donation, Rate
from decimal import Decimal, ROUND_HALF_UP
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.core.mail import EmailMessage

# Create your views here.

# def custom_login(request,**kwargs):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         return login(request,**kwargs)


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate Your Account'
                message = render_to_string('users/activate_account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(email_subject, message, to=[to_email])
                email.send()
                return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
        else:
            form = SignUpForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if request.user.is_authenticated:
        return redirect('/')
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return HttpResponse('Your account has been activate successfully')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required
def userProfile(request, uid):
    user2 = get_object_or_404(User, id=uid)
    categories = Category.objects.all()
    projects = Project.objects.all().filter(user_id=uid)
    for p in projects:

        donation_sum = p.donation_set.all().aggregate(Sum("amount"))['amount__sum']
        p.donation_sum = donation_sum if donation_sum else 0
        p.delete_flag = True if p.donation_sum <= p.target * 0.25 else False

    context = {
        'userprofile': user2,
        'userProject': projects,
        'categories': categories,
        'donations': Donation.objects.all().filter(user_id=uid),
        'latestFiveList': Project.objects.extra(order_by=['created_at'])
    }
    return render(request, "users/profile.html", context)


@login_required
def editProfile(request, uid):
    if request.user.profile.id != uid:
        raise Http404("Not Found")
    user2 = get_object_or_404(User, id=uid)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user2)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=user2.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile', uid=uid)

    else:
        u_form = UserUpdateForm(instance=user2)
        p_form = ProfileUpdateForm(instance=user2.profile)
    context = {
        "userprofile": user2,
        # "categories": categories,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "users/edit_profile.html", context)


@login_required
def deleteuser(request, uid):
    user2 = get_object_or_404(User, id=uid)
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=user2)
        user2.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('/')
    else:
        delete_form = UserDeleteForm(instance=user2)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'users/delete_account.html', context)
