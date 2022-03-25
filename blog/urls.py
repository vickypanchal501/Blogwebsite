from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.home_site, name= 'home'),
    path('blogus/',views.BlogUs, name= 'blogus'),
    path('posts/',views.Posts, name= 'posts')
]
