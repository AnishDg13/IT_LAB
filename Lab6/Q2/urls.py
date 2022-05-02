"""
Definition of urls for Q2.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
 path('',views.formView, name = 'formView'),
 url(r'^login/', views.login, name = 'login'),
 url(r'^logout/', views.logout, name = 'logout'),
]

