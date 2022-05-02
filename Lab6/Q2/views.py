"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

check=0

def login(request):
 name = 'Enter Name'
 roll = 'None'
 subject = 'None'
 print('Initially',str(request.method))
 while True:
     if request.method == 'POST':
         
         MyLoginForm = LoginForm(request.POST)
         
         if MyLoginForm.is_valid():
             name = MyLoginForm.cleaned_data['name']
             request.session['name'] = name
             roll = MyLoginForm.cleaned_data['roll']
             request.session['roll'] = roll
             subject = MyLoginForm.cleaned_data['subject']
             request.session['subject'] = subject
             print('Trying:')
             print(subject)
             print(type(subject))
         break
     else:
         print("HERE!!!!!!!")
         MyLoginForm = LoginForm()
 return render(request, 'app/loggedin.html', {"name":name,"roll":roll,"subject":subject})

def formView(request):
 global check
 if check==0:
     if request.session.has_key('name'):
         del request.session['name']
     check=1
 if request.session.has_key('name'):
     print("here")
     name = request.session['name']
     roll = request.session['roll']
     subject = request.session['subject']
     form = LoginForm(request.POST or None)
     context = {"name":name,"roll":roll,"subject":subject}

     return render(request, 'app/login.html', context)
 else:
    context = {"name":"Enter name","roll":"None","subject":"None"}
    form = LoginForm(request.POST or None)
    #context['form'] = form 
    print('COmes here first.')
    return render(request, 'app/login.html', context)


def logout(request):
 try:
    del request.session['username']
 except:
    pass
 return HttpResponse("<strong>You are logged out.</strong>")


