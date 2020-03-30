from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views
app_name = "users"

urlpatterns = [
    path('profile/<int:uid>', views.userProfile , name='profile'),
    path('edit<int:uid>', views.editProfile , name='edit'),
    path('signup',views.signup, name='signup'),

]
