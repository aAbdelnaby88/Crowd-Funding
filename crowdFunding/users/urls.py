from django.urls import path , include
from . import views
app_name = "users"

urlpatterns = [
    path('profile/<int:id>', views.userProfile , name='profile'),
    path('signup',views.signup, name='signup'),

]
