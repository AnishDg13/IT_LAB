"""
Definition of models.
"""

from django.db import models
from django import forms
from django.db.models import constraints


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    # noOfVisits is sum of all page views of the category
    noOfVisits = models.IntegerField(default=0)
    noOfLikes = models.IntegerField()
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #multiple pages can belong to the same category
    title = models.CharField(max_length=30)
    # views:can set a default as well as it gets incremented if we click on the link
    views = models.IntegerField(default=0)
    url = models.CharField(max_length=50, default="https://www.google.com")
    class Meta:
        ordering = ['views']
    def __str__(self):
        return self.title#what to print when an object of a class is printed

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('noOfVisits',)