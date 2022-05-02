"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from .forms import MobileForm


def page1(request):
    form = MobileForm()
    return render(request, 'app/pageOne.html', {'form': form})

def page2(request):
    manufacturer = ""
    device = ""
    quantity = 0
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            device = form.cleaned_data['device']
            quantity = form.cleaned_data['quantity']
    else:
        form = MobileForm()

    unit_price=0

    list1 = [ 'HP', 'Nokia', 'Samsung', 'Motorola', 'Apple']
    laptop_list=[20,30,40,50,60]
    mobile_list=[10,20,30,40,50]
    
    for i in list1:
        if manufacturer==i:
            index=list1.index(i)
            if device=='Laptop':
                unit_price=laptop_list[index]
            else:
                unit_price=mobile_list[index]
    context = {'manufacturer': manufacturer,'device': device[0], 'quantity': quantity,'amountForOne': unit_price}
    return render(request, 'app/pageTwo.html', context)
