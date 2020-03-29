from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(required=False,help_text='Optional.')
    phone = forms.CharField(max_length=11,required=False, help_text='Optional.')
    # user_image = forms.ImageField(label = "upload your image",required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )








# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = models.Profile
#         fields = ['user_image', 'birth_date', 'country', 'facebook', 'phone']
