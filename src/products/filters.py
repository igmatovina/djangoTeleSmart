import django_filters
from django_filters import DateFilter, CharFilter
from django_filters import rest_framework as filters

from .models import *

class DeviceFilter(django_filters.FilterSet):
    class Meta:
        model = Device
        fields = {
            'description': ['contains'],
            'mac': ['contains'],
            'customer' : ['exact'],
            'device_model' : ['exact'],
            }
