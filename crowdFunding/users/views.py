from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth import  login , authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .token_generator import account_activation_token
from django.core.mail import EmailMessage
# Create your views here.

def index(request):
    return (request,"users/test.html")

def userProfile(request,id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get(user_name=id)
    context={'profile' : profile , 'user' : user}
    return render(request,"users/profile.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request, f'Your account has been created!')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


 # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # current_site = get_current_site(request)
            # email_subject = 'Activate Your Account'
            # message = render_to_string('activate_account.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            #     'token': account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(email_subject, message, to=[to_email])
            # email.send()
            # return HttpResponse('We have sent you an email, please confirm your email address to complete registration')

# def activate_account(request, uidb64, token):
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Your account has been activate successfully')
#     else:
#         return HttpResponse('Activation link is invalid!')


