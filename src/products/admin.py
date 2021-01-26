from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(DeviceModel)
admin.site.register(DeviceVendor)
admin.site.register(Device)
admin.site.register(Extension)
admin.site.register(Dss)
