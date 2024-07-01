from django.contrib import admin
from .models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Task, TaskAdmin)

class SiteAdmin(admin.ModelAdmin):
  readonly_fields = ('name', )

admin.site.register(Site, SiteAdmin)

class RackAdmin(admin.ModelAdmin):
  readonly_fields = ('name', 'site')

  #def formfield_for_foreignkey(self, db_field, request, **kwargs):
  #    if db_field.name == "site":
  #        kwargs["queryset"] = Site.objects.select_related("name")
  #    return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Rack, RackAdmin)

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
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "device":
            kwargs["queryset"] = Device.objects.select_related("name")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Case, CaseAdmin)

admin.site.register(Avatar)