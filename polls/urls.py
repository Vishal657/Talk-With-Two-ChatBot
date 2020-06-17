
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('home',views.home1 , name='home1'),
    path('bot11',views.bot11 , name='bot11'),
    path('bot22',views.bot22 , name='bot22'),
    path('bot33',views.bot33 , name='bot33'),
    
]
