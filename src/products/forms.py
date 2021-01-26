from django.forms import ModelForm
from .models import Device, Customer, Dss ,DeviceVendor ,DeviceModel


class DeviceForm(ModelForm):
	class Meta:
		model = Device
		fields = '__all__'

class DssForm(ModelForm):
	class Meta:
		model = Dss
		fields = '__all__'