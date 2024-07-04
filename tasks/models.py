from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey # https://django-smart-selects.readthedocs.io/en/latest/usage.html#

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  completed = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title + ' - ' + self.user.username
  
class Site(models.Model):

  siteId = models.CharField(max_length=6)
  name = models.CharField(max_length=20)
  address = models.CharField(max_length=30)
  city = models.CharField(max_length=20)
  country = models.CharField(max_length=20)
  switchowner = models.CharField(max_length=30)
  contact = models.IntegerField(default=0)
  siteImage = models.ImageField(upload_to='sites', blank=True, null=True, default="/media/static/default.png") # default=""
  
  def __str__(self):
    return self.name
  
  class Meta():
    verbose_name = 'Site'
    verbose_name_plural = 'Sites'
    ordering = ('siteId', 'name')
    unique_together = ('siteId', 'name')

class Rack(models.Model):

  rackId = models.CharField(max_length=6)
  name = models.CharField(max_length=20)
  site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, related_name='racks')
  rackImage = models.ImageField(upload_to='racks', blank=True, null=True, default="/media/static/default.png") # default=""

  #def save(self, *args, **kwargs):
  #  self.site = self.site.name
  #  super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.name}"

  class Meta():
    verbose_name = 'Rack'
    verbose_name_plural = 'Racks'
    ordering = ('rackId', 'name')
    unique_together = ('rackId', 'name')
    
class Vendor(models.Model):

  vendorId = models.CharField(max_length=6)
  name = models.CharField(max_length=20)
  email = models.EmailField()
  contact = models.IntegerField()
  link = models.URLField(max_length=200, blank=True)
  vendorImage = models.ImageField(upload_to='vendors', blank=True, null=True, default="/media/static/default.png")

  def __str__(self):
    return self.name
  
  class Meta():

    verbose_name = 'Vendor'
    verbose_name_plural = 'Vendors'
    ordering = ('vendorId', 'name')
    unique_together = ('vendorId', 'name')

class Device(models.Model):

  deviceId = models.CharField(max_length=6)
  name = models.CharField(max_length=20)
  category = models.CharField(max_length=20)
  model = models.CharField(max_length=20)
  serialNumber = models.CharField(max_length=30)
  site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
  rack = models.ForeignKey(Rack, on_delete=models.CASCADE, null=True, related_name='devices')
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
  deviceImage = models.ImageField(upload_to='devices', blank=True, null=True, default="/media/static/default.png")

  #def save(self, *args, **kwargs):
  #  self.site = self.site.name
  #  self.rack = self.rack.name
  #  self.vendor = self.vendor.name
  #  super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.name}"

  class Meta():

    verbose_name = 'Device'
    verbose_name_plural = 'Devices'
    ordering = ('deviceId', 'name')
    unique_together = ('deviceId', 'name')

class Operator(models.Model):

  operatorId = models.CharField(max_length=6)
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  email = models.EmailField()
  contact = models.IntegerField()
  backOffice = models.CharField(max_length=20)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  operatorImage = models.ImageField(upload_to='operators', blank=True, null=True, default="/media/static/default.png")
  # site = models.ForeignKey(Site, on_delete=models.CASCADE)
    
  def __str__(self):
    return self.firstName + ' ' + self.lastName + ' - ' + self.backOffice + ' - ' + self.user.username

  class Meta():

    verbose_name = 'Operator'
    verbose_name_plural = 'Operators'
    ordering = ('operatorId', 'firstName', 'lastName')
    unique_together = ('operatorId', 'firstName', 'lastName')

class Case(models.Model):
  SEVERITIES = (
    ('1', "1. Not classified"),
    ('2', "2. Information"),
    ('3', "3. Warning"),
    ('4', "4. Average"),
    ('5', "5. High"),
    ('6', "6. Disaster")
  )
  caseId = models.CharField(max_length=6)
  description = models.CharField(max_length=20)
  severity = models.CharField(choices=SEVERITIES, max_length=2, null=True)
  site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, editable=False)
  rack = models.ForeignKey(Rack, on_delete=models.CASCADE, null=True, editable=False) 
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, editable=False)
  device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
  operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True)
  caseImage = models.ImageField(upload_to='cases', blank=True, null=True, default="/media/static/default.png")

  def save(self, *args, **kwargs):
    self.site = self.device.site
    self.rack = self.device.rack
    self.vendor = self.device.vendor
    super().save(*args, **kwargs)
    
  def __str__(self):
    return f'{self.caseId} - {self.device.name} - {self.severity} - {self.description} - {self.operator.user.username}'

  class Meta():

    verbose_name = 'Case'
    verbose_name_plural = 'Cases'
    ordering = ('caseId', 'description')
    unique_together = ('caseId', 'description')

class Avatar(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  userImage = models.ImageField(upload_to='images', blank=True, null=True)

  def __str__(self):
      return self.user + ' - ' + self.userImage