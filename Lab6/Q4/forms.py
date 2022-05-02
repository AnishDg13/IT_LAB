"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

CHOICES1 = (('HP', 'HP'), ('Nokia', 'Nokia'), ('Samsung', 'Samsung'),('Motorola', 'Motorola'), ('Apple', 'Apple'))
CHOICES2 = (('Laptop', 'Laptop'), ('Mobile', 'Mobile'))

class MobileForm(forms.Form):
    manufacturer = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': "custom-radio-list"}), choices=CHOICES1)
    device = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES2)
    quantity = forms.IntegerField(label='Quantity :')