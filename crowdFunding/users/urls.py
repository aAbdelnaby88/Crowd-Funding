from django.urls import path , include
# from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('profile/<int:uid>', views.userProfile , name='profile'),

    path('edit/<int:uid>', views.editProfile , name='edit'),

    path('signup',views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('', views.index, name='index'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate_account, name='activate')

]
