"""
Definition of urls for Q4.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.page1, name='page1'),
    path('choose', views.page1, name='page1'),
    path('results', views.page2, name='page2'),

]
