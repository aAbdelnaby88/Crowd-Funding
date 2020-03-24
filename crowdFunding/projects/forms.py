from django import forms
from django.utils import timezone
from .models import Project , ProjectPicture


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title','details','target','start_date','end_date' ,'category' , 'tags']
        # model = ProjectPicture
        # fields = ['img_url']