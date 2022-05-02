"""
Definition of urls for Solved_Hopeful.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path,re_path
from app.views import archive,create_blogpost
from app import forms, views
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', archive, name='archive'),
    path('blog/create/', create_blogpost, name='create_blogpost'),
]
