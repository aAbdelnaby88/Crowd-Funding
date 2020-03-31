from django import forms
from django.utils import timezone
from .models import Project , ProjectPicture
from django.forms import ModelForm 


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title','details','target','start_date','end_date' ,'category' , 'tags']
        

class ImageForm(forms.ModelForm):
    #image = forms.ImageField(label='Image')    
    class Meta:
        model = ProjectPicture
        fields = ['img_url', ]

