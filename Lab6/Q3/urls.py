"""
Definition of urls for Q3.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.register, name='register'),
    path('register', views.register, name='register'),
    path('success',  views.success, name='success'),
]
