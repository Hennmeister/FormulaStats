from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Driver

def index(request):
    driver_list = Driver.objects.all()
    context = {
        'driver_list': driver_list,
    }
    return render(request, 'drivers/index.html', context)

def driverInfo(request, driver_id: int):
    context = {
        'driver': Driver.objects.get(pk=driver_id),
    }
    return render(request, 'drivers/driverStats.html', context)

