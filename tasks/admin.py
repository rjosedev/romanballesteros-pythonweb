from django.contrib import admin
from .models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Task, TaskAdmin)

class SiteAdmin(admin.ModelAdmin):
  readonly_fields = ('name', )

admin.site.register(Site, SiteAdmin)

class VendorAdmin(admin.ModelAdmin):
  readonly_fields = ('name', )

admin.site.register(Vendor, VendorAdmin)

class DeviceAdmin(admin.ModelAdmin):
  readonly_fields = ('name', )

admin.site.register(Device, DeviceAdmin)

class OperatorAdmin(admin.ModelAdmin):
  readonly_fields = ('firstName', )

admin.site.register(Operator, OperatorAdmin)

class CaseAdmin(admin.ModelAdmin):
  readonly_fields = ('description', )

admin.site.register(Case, CaseAdmin)

admin.site.register(Avatar)