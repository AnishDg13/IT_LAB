"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):

 name = forms.CharField(widget=forms.Textarea)
 roll = forms.CharField(widget=forms.Textarea)
 GEEKS_CHOICES =(("1", "Math"),("2", "DSA"),("3", "OOP"),("4", "ADSA"),("5", "FLAT"),)
 subject = forms.ChoiceField(choices = GEEKS_CHOICES)
