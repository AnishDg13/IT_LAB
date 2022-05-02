"""
Definition of urls for Q2.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('list', views.list, name='list'),
    path('worksForm', views.worksForm, name='worksForm'),
    path('livesForm', views.livesForm, name='livesForm'),
    path('worksSubmit',views.worksSubmit,name='worksSubmit'),
    path('livesSubmit',views.livesSubmit,name='livesSubmit'),
]
