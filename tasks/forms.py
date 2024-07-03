from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ['siteId', 'country', 'city', 'address', 'contact', 'switchowner', 'name', 'siteImage']

class SiteEditForm(ModelForm):
    class Meta:
        model = Site
        fields = ['siteId', 'name', 'address', 'city', 'country', 'switchowner', 'contact', 'siteImage']

class RackForm(ModelForm):
    class Meta:
        model = Rack
        fields = ['rackId', 'site', 'name', 'rackImage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['site'].queryset = Site.objects.all()

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendorId','name', 'email', 'contact', 'link', 'vendorImage']

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['deviceId', 'site', 'rack', 'vendor', 'category', 'name', 'model', 'serialNumber', 'deviceImage']

    # def __init__(self, site_id, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['rack'].queryset = Rack.objects.filter(site_id=site_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rack'].queryset = Rack.objects.all()
    
        if 'site' in self.data:
            try:
                site_id = int(self.data.get('site'))
                self.fields['rack'].queryset = Rack.objects.filter(site_id=site_id)
            except (ValueError, TypeError):
                pass  # Handle the error as you need

        elif self.instance.pk:
            self.fields['rack'].queryset = self.instance.rack.site.racks.all()

class OperatorForm(ModelForm):
    class Meta:
        model = Operator
        fields = ['operatorId', 'firstName', 'lastName', 'email', 'contact', 'backOffice', 'user', 'operatorImage']

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ['caseId', 'device', 'severity', 'description', 'operator', 'caseImage']

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text = "",
        widget = forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2
