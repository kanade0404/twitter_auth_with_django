from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
import django.contrib.auth.views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('top/', views.top_page, name="top_page"),
    path('login/', django.contrib.auth.views.login,
         {
             'template_name': 'login/index.html',
         }, name='login'),
    path('logout/', django.contrib.auth.views.logout,
         {
             'template_name': 'logout/index.html',
         }, name='logout'),

]