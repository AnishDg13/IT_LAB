"""
Definition of urls for Additional1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from app import forms, views


urlpatterns = [
    path('entry',views.Entry,name='Entry'),
    path('list',views.show,name='show'),
    path('temp',views.temp,name='temp'),
    path('update',views.update,name='temp'),
    path('delete',views.delete,name='temp'),
]
