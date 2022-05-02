from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.models import Category, Page, CategoryForm, PageFormdef pageList(request):
    if request.method == 'POST':
        category = request.POST['category']
        pages = Page.objects.filter(category__name__startswith=category)
        return render(request, 'app/table_page.html', {'pages': pages})
    pages = Page.objects.all()[:10]
    return render(request, 'app/table_page.html', {'pages': pages})def forms(request):
    return render(request, 'app/form_page.html', {'categoryForm':CategoryForm(), 'pageForm': PageForm()})

def pageSubmit(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.save()
            category = Category.objects.get(name=page.category)
            category.noOfVisits += page.views
            category.save()
            print(category)
            return HttpResponseRedirect('/list')
        else:
            return render(request, 'app/form_page.html', {'categoryForm':CategoryForm(), 'pageForm': PageForm()})

def categorySubmit(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            category.noOfVisits = 0
            category.save()
            return HttpResponseRedirect('/list')
        else:
            return render(request, 'app/form_page.html', {'categoryForm':CategoryForm(), 'pageForm': PageForm()})def updateViews(request, pk1):
    page = Page.objects.get(pk=pk1)
    page.views += 1
    page.save()
    category = Category.objects.get(name=page.category)
    category.noOfVisits += 1
    category.save()
    return HttpResponseRedirect(page.url)