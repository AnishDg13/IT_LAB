"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class RegForm(forms.Form):
    #title = forms.CharField()
    #description = forms.CharField()
    #views = forms.IntegerField()
    #available = forms.BooleanField()
    model = forms.CharField(widget=forms.TextInput)
    CHOICES= (('1','BrandA'), ('2','BrandB'), ('3','BrandC'),)
    select = forms.ChoiceField(widget=forms.Select, choices=CHOICES)