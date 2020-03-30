from django.urls import path
from . import views

urlpatterns = [

    path('projectDetails/<int:id>',views.showProject,name="show_proj"),
    path('showCategory/<int:id>',views.showCategoryProjects),
    path('<int:id>/comment', views.create_comment, name = 'create_comment'),
    path('create', views.create)

]
