from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Driver
from .getData import getData
import operator


def index(request):
    driver_list = sorted(Driver.objects.all(),
                         key=operator.attrgetter('last_name'))
    context = {
        'driver_list': driver_list,
    }
    return render(request, 'drivers/index.html', context)


def driverInfo(request, driver_id: int):
    driver = Driver.objects.get(pk=driver_id)
    race_data = getData(driver.last_name)

    context = {
        'driver': Driver.objects.get(pk=driver_id),
        'recent_results': race_data.get('results'),
        'track_names': race_data.get('names')
    }

    return render(request, 'drivers/driverStats.html', context)

