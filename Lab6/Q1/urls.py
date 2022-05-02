"""
Definition of urls for Q1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

app_name='Trial'
urlpatterns = [
    path('', views.first, name='first'),
    path('/page2i',views.page2,name='page2')
]
