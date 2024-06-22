from django.db import models
from django.contrib.auth.models import User

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
  siteImage = models.ImageField(upload_to='sites', blank=True, null=True) # default=""
  
  def __str__(self):
    return self.siteId + ' - ' + self.name
  
  class Meta():
    verbose_name = 'Site'
    verbose_name_plural = 'Sites'
    ordering = ('siteId', 'name')
    unique_together = ('siteId', 'name')
    
class Vendor(models.Model):

  vendorId = models.CharField(max_length=6)
  name = models.CharField(max_length=20)
  email = models.EmailField()
  contact = models.IntegerField()
  vendorImage = models.ImageField(upload_to='vendors', blank=True, null=True)

  def __str__(self):
    return self.vendorId + ' - ' + self.name
  
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
  rack = models.CharField(max_length=30)
  site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
  deviceImage = models.ImageField(upload_to='devices', blank=True, null=True)

  def __str__(self):
    return self.deviceId + ' - ' + self.name

  class Meta():

    verbose_name = 'Device'
    verbose_name_plural = 'Devices'
    ordering = ('deviceId', 'name', 'category')
    unique_together = ('deviceId', 'name', 'category')

class Operator(models.Model):

  operatorId = models.CharField(max_length=6)
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  email = models.EmailField()
  contact = models.IntegerField()
  backOffice = models.CharField(max_length=20)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  operatorImage = models.ImageField(upload_to='operators', blank=True, null=True)
  # site = models.ForeignKey(Site, on_delete=models.CASCADE)
    
  def __str__(self):
    return self.operatorId + ' - ' + self.firstName + ' - ' + self.lastName

  class Meta():

    verbose_name = 'Operator'
    verbose_name_plural = 'Operators'
    ordering = ('operatorId', 'firstName', 'lastName')
    unique_together = ('operatorId', 'firstName', 'lastName')

class Case(models.Model):
  SEVERITIES = (
    ('1', "Not classified"),
    ('2', "Information"),
    ('3', "Warning"),
    ('4', "Average"),
    ('5', "High"),
    ('6', "Disaster")
  )
  caseId = models.CharField(max_length=6)
  description = models.CharField(max_length=20)
  severity = models.CharField(choices=SEVERITIES, max_length=2, null=True)
  site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
  device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
  operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True)
  caseImage = models.ImageField(upload_to='cases', blank=True, null=True)
    
  def __str__(self):
    return f'{self.caseId} - {self.description} - {self.severity} - {self.site} - {self.vendor} - {self.device} - {self.operator}'

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