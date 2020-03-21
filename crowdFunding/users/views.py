from django.shortcuts import render

<<<<<<< HEAD
from django.http import HttpResponse
# Create your views here.

def userProfile(request):
    return HttpResponse('<h1>user profile<h1>')
=======
def index(request):
    return render(request,"users/login.html")
>>>>>>> fdb86578424546aa969a05f5a73be29701e068a0
