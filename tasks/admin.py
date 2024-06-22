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

admin.site.register(Avatar)