"""
Definition of urls for Q1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from app import forms, views


urlpatterns = [
    path('list', views.pageList, name='pageList'),
    path('forms', views.forms, name='forms'),
    path('categorySubmit', views.categorySubmit, name='categorySubmit'),
    path('pageSubmit', views.pageSubmit, name='pageSubmit'),
    path('<int:pk1>/updateViews/', views.updateViews, name='updateViews'),
]
