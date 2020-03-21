from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def userProfile(request):
    return HttpResponse('<h1>user profile<h1>')
