from django.urls import path
from . import views

urlpatterns = [
    path('projectDetails/<int:id>',views.showProject,name="show_proj"),
    path('showCategory/<int:id>',views.showCategoryProjects),
    path('create/', views.create),
]

