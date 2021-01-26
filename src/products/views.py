from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .filters import DeviceFilter
from .forms import DeviceForm
from django.core import serializers
from django.core.files import File
from datetime import datetime


def home(request):
    devices=Device.objects.all()
    customer=Customer.objects.all()
    dsss=Dss.objects.all()
    extensions=Extension.objects.all()
    device_models=DeviceModel.objects.all()
    vendors=DeviceVendor.objects.all()
    dsss = Dss.objects.all()

    myFilter = DeviceFilter(request.GET, queryset=devices)
    devices=myFilter.qs

    context = {'devices':devices, 'customer':customer, 'myFilter':myFilter, 'device_models':device_models, 'vendors':vendors, 'extensions':extensions}

    return render(request, "home.html", context)



def adminDevice(request, pk):
    device = Device.objects.get(id=pk)
    customer=Customer.objects.all()
    dsss = device.dss_set.all()
    extensions = device.extension_set.all()

    total_dss= dsss.count()
    form = DeviceForm(instance=device)

    context = {'device':device, 'dsss':dsss, 'total_dss':total_dss, 'extensions':extensions}
    return render(request, 'dashboard.html', context)


def deleteDss(request, pk):
    dss = Dss.objects.get(id=pk)
    if request.method == "POST":
        dss.delete()
        return redirect('/')
        
    context = {'item':dss}
    return render(request, 'delete.html', context)

def createDss(request, pk):
    DssFormSet = inlineformset_factory(Device, Dss, fields=('dss_type', 'label', 'key', 'value'), extra=1)
    device = Device.objects.get(id=pk)
    device.cfg_last_update = datetime.now()
    device.save()
    formset = DssFormSet(queryset=Dss.objects.none(),instance=device)
    if request.method == 'POST':
        formset = DssFormSet(request.POST, instance=device)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form':formset}
    return render(request, 'dss_form.html', context)

def editDevice(request, pk):

    device = Device.objects.get(id=pk)
    form = DeviceForm(instance=device)
    device.cfg_last_update = datetime.now()
    device.save()
    
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('admin_device', pk)
            
    context = {'form':form}
    return render(request, 'device_form.html', context)

def config(request, pk):
    device = Device.objects.get(id=pk)
    device.cfg_last_update = datetime.now()
    device.save()
    data = serializers.serialize("xml", Device.objects.all())
    f = open('templates/events.xml', 'w')
    myfile = File(f)
    myfile.write(data)
    myfile.close()
    return HttpResponse("xml saved to templates/events.xml! ")








