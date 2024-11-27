from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',Register  , name='register'),
    path('login/', login_page , name='login'),
    path('dashboard/',dashboard,name='dashboard')
   
]
