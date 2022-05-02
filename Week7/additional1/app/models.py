"""
Definition of models.
"""

from django.db import models
from django import forms

# Create your models here.
class Human(models.Model):
    firstname = models.CharField(max_length=50,primary_key=True)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        ordering = ['firstname']
    def __str__(self):
        return self.firstname

 
class HumanForm(forms.ModelForm):
    class Meta:
        model=Human
        fields='__all__'

