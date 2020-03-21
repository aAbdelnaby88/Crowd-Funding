<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.userProfile)
=======
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),

>>>>>>> fdb86578424546aa969a05f5a73be29701e068a0
]