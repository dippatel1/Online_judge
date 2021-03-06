from re import template
import django
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_view
app_name = 'user'
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
     path('login/',auth_view.LoginView.as_view(template_name='user/login.html'),name="login"),
      path('logout/',auth_view.LogoutView.as_view(template_name='user/logout.html'),name="logout"),
     path('profile/',views.profile,name="profile"),
      path('page/',include('oj.urls')),
]