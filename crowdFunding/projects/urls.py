from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.showProject),
    path('<int:id>/comment', views.create_comment, name = 'create_comment'),
    path('create', views.create)
]
