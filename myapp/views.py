from django.shortcuts import render, redirect
from .models import Names

# Create your views here.
def default_name(request):
    names = Names.objects.all()
    return render(request, 'names.html', {'names': names}) 


def home(request):
    data = Names.objects.all()
    for i in data:
        i.name = i.new_method()
        i.save()
    return render(request, 'home.html')

def a2(request):
    for i in data:
        if i.pk % 2 == 0:
            i.delete()