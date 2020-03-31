from django.urls import path
from . import views

urlpatterns = [

    path('projectDetails/<int:id>',views.showProject,name="show_proj"),
    path('showCategory/<int:id>',views.showCategoryProjects),
    path('<int:id>/comment', views.create_comment, name = 'create_comment'),
    path('<int:id>/report_pro', views.report_project, name = 'report_project'),
    path('<int:id>/report_com', views.report_comment, name = 'report_comment'),
    path('create', views.create)

]
