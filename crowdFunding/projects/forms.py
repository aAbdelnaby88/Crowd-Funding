from django import forms
from django.utils import timezone
from .models import Project , Category


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title','details','target','start_date','end_date' ,'category' , 'tags']