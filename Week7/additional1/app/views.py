"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.models import Human,HumanForm

def Entry(request):
    print('Inside Entry')
    if request.method=='POST':
        print('In here!!!!')
        form = HumanForm(request.POST)
        if form.is_valid():
            
            entry = form.save(commit=False)
            entry.save()
            return HttpResponseRedirect('/list')
    return render(request,'app/enter.html',{'form':HumanForm()})

def show(request):
    obj=Human.objects.all()
    obj=Human.objects.all()
    obj2=obj[0]
    return render(request,'app/show.html',{'humans':obj,'current':obj2})

def temp(request):
    if(request.method=='POST'):
        selected=request.POST['selected']
        print(selected)
        current=1
        obj=Human.objects.all()
        for o in obj:
            if o.firstname==selected:
                current=o
        print('CUrrent object name:',current.firstname)
        #current=obj[0]
        return render(request,'app/show.html',{'humans':obj,'current':current})

def update(request):
    if request.method=='POST':
        name=request.POST['selected']
        updated_address=request.POST['pg_address']
        updated_city=request.POST['pg_city']
        Human.objects.filter(firstname=name).update(address=updated_address,city=updated_city)
        return HttpResponseRedirect('list')

def delete(request):
    if request.method=='POST':
        name=request.POST['selected']
        Human.objects.filter(firstname=name).delete()
        return HttpResponseRedirect('list')