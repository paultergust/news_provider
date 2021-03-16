from django.contrib import admin
from django.urls import path

from rest_framework.authtoken import views as drf_views

from . import views

urlpatterns = [
        path('sign-up/', views.signup, name='signup'),
        path('login/', drf_views.obtain_auth_token, name='login'),
        path('articles/', views.articles, name='articles'),
]
