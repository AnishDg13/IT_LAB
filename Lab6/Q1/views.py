"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import RegForm

def page2(request): 
 context = {}
 brand=request.POST.get('select')
 model=request.POST.get('model')
 context={"Brand":brand[0],"Model":model}
 return render(request, "app/page_2.html", context)


def first(request):
    context = {}
    form = RegForm(request.POST or None)
    context['form'] = form 
    return render(request,'app/page1.html',context)