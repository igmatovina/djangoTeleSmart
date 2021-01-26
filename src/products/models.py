from django.db import models
from enum import Enum




class Customer(models.Model):
    description = models.CharField(max_length=20, null=True, blank=True)
    def __unicode__(self):
        return self.description


FORMATA = 'FMA'
FORMATB = 'FMB'
FORMAT_CHOICES = [
    (FORMATA, 'FormatA'),
    (FORMATB, 'FormatB'),
]

class DeviceModel(models.Model):
    name = models.CharField(max_length=15, null=True, blank=True)
    dss = models.BooleanField(default=False)
    device_format = models.CharField(
        max_length=255,
        choices=FORMAT_CHOICES,
        default=FORMATA,
    )


class DeviceVendor(models.Model):
    name = models.CharField(max_length=15, null=True, blank=True)

class Device(models.Model):
    mac = models.CharField(max_length=10, unique=True)    
    description = models.CharField(max_length=20, null=True, blank=True)
    cfg_last_update = models.DateTimeField(auto_now_add=True, null=True)

    customer = models.ForeignKey(Customer,  null=True, on_delete=models.SET_NULL)     
    device_model = models.ForeignKey(DeviceModel,  null=True, on_delete=models.SET_NULL)     
    vendor = models.ForeignKey(DeviceVendor,  null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return "%s > %s" % (self.customer, self.device_model, self.vendor)


class Extension(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)
    extension = models.IntegerField(blank=True, null=True)
    device = models.ForeignKey(Device,  null=True, on_delete=models.SET_NULL)   

class Dss(models.Model):
    DSS_TYPE=(
        ('BLF','BLF'),
        ('SPD','SPD'),
    )

    dss_type = models.CharField(max_length=10, null=True, choices=DSS_TYPE)
    label = models.CharField(max_length=10, null=True, blank=True)
    key = models.CharField(max_length=10, null=True, blank=True)
    value = models.IntegerField(blank=True, null=True)

    device = models.ForeignKey(Device,  null=True, on_delete=models.SET_NULL)   



# Create your models here.
