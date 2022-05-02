"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

class RegForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput,label='Username : ')
    email= forms.CharField(widget=forms.EmailInput, label='EMail : ',required=False)
    password = forms.CharField(widget=forms.PasswordInput,label='Password : ',required=False)
    contact = forms.CharField(widget = forms.NumberInput,label='Contact No : ', required=False)

