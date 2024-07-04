"""
URL configuration for projectfollowup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('pages/', views.pages, name='pages'),
    path('about/', views.about, name='about'),
    path('only_staff/', views.only_staff, name='only_staff'),
    path('smart_selects/', include('smart_selects.urls')),
    
    ### USER ###
    path('admin/', admin.site.urls),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('edit_profile/', views.editprofile, name='edit_profile'),
    path('logout/', views.signout, name='logout'),

    ### TASK ###
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('task_table/', views.task_table, name='task_table'),
    path('task_create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.task_complete, name='task_complete'),
    path('tasks/<int:task_id>/delete', views.task_delete, name='task_delete'),

    ### SITE ###
    path('sites/', views.sites, name='sites'),
    path('site_table/', views.site_table, name='site_table'),
    path('site_create/', views.site_create, name='site_create'),
    path('sites/<int:site_id>', views.site_detail, name='site_detail'),
    path('sites/<int:site_id>/delete', views.site_delete, name='site_delete'),

    ### RACK ###
    path('racks/', views.racks, name='racks'),
    path('rack_table/', views.rack_table, name='rack_table'),
    path('rack_create/', views.rack_create, name='rack_create'),
    path('racks/<int:rack_id>', views.rack_detail, name='rack_detail'),
    path('racks/<int:rack_id>/delete', views.rack_delete, name='rack_delete'),

    ### VENDOR ###
    path('vendors/', views.vendors, name='vendors'),
    path('vendor_table/', views.vendor_table, name='vendor_table'),
    path('vendor_create/', views.vendor_create, name='vendor_create'),
    path('vendors/<int:vendor_id>', views.vendor_detail, name='vendor_detail'),
    path('vendors/<int:vendor_id>/delete', views.vendor_delete, name='vendor_delete'),

    ### DEVICE ###
    path('devices/', views.devices, name='devices'),
    path('device_table/', views.device_table, name='device_table'),
    path('device_create/', views.device_create, name='device_create'),
    path('devices/<int:device_id>', views.device_detail, name='device_detail'),
    path('devices/<int:device_id>/delete', views.device_delete, name='device_delete'),

    ### OPERATOR ###
    path('operators/', views.operators, name='operators'),
    path('operator_table/', views.operator_table, name='operator_table'),
    path('operator_create/', views.operator_create, name='operator_create'),
    path('operators/<int:operator_id>', views.operator_detail, name='operator_detail'),
    path('operators/<int:operator_id>/delete', views.operator_delete, name='operator_delete'),
    
    ### CASE ###
    path('cases/', views.cases, name='cases'),
    path('case_table/', views.case_table, name='case_table'),
    path('case_create/', views.case_create, name='case_create'),
    path('cases/<int:case_id>', views.case_detail, name='case_detail'),
    path('cases/<int:case_id>/delete', views.case_delete, name='case_delete'),
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)