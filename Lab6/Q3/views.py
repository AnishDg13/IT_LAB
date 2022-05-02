"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import RegForm

def register(request):
    form=RegForm()
    return render(request,"app/register.html",{'form':form})


def success(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
    else:
        form = RegForm()
    context = {'username':username,'email':email,'contact':contact}
    return render(request,"app/success.html",context)