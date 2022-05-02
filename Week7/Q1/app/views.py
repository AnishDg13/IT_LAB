from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.models import WORKS, LIVES, LivesForm, WorksForm

def list(request):
    if request.method == 'POST':
        company = request.POST['company']
        print('Company Name is',company)
        people=[]
        for obj in WORKS.objects.all():
            if obj.company_name==company:
                people.append(obj.person_name)
        list_of_people=[]

        print('list of people are:')
        for p in people:
            print(str(p))

        for person in people:

            for obj in LIVES.objects.all():
                if str(obj.person_name)==(str(person)):
                    print('In Here!!!')
                    list_of_people.append(obj)
        if company=='':
            list_of_people=LIVES.objects.all()
        return render(request, 'app/show.html', {'persons': list_of_people})
    people = LIVES.objects.all()[:10]
    return render(request, 'app/show.html', {'persons': people})

def worksForm(request):
    return render(request, 'app/worksForm.html', {'form': WorksForm()})
def livesForm(request):
    return render(request, 'app/livesForm.html', {'form':LivesForm()})

def worksSubmit(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            works = form.save(commit=False)
            works.save()
            return HttpResponseRedirect('/list')
        else:
            return render(request, 'app/worksForm.html', {'form':WorksForm()})

def livesSubmit(request):
    if request.method == 'POST':
        form = LivesForm(request.POST)
        if form.is_valid():
            lives = form.save(commit=False)
            lives.save()
            return HttpResponseRedirect('/list')
        else:
            return render(request, 'app/livesForm.html', {'form':LivesForm()})