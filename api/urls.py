from django.contrib import admin
from django.urls import path

from rest_framework.authtoken import views as drf_views

from . import views

urlpatterns = [
        path('sign-up/', views.signup, name='signup'),
        path('login/', drf_views.obtain_auth_token, name='login'),
        path('articles/', views.articles, name='articles'),
        path('admin/articles/', views.ArticlesList.as_view(), name='articles_list'),
        path('admin/articles/<int:pk>', views.ArticleView.as_view(), name='article_view'),
        path('admin/authors/', views.AuthorsList.as_view(), name='authors_list'),
        path('admin/authors/<int:pk>', views.AuthorView.as_view(), name='author_view'),
]
