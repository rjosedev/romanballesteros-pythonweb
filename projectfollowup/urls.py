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
    path('profile_edit/', views.profile_edit, name='profile_edit'),
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
    path('site_scroll/', views.site_scroll, name='site_scroll'),
    path('site_table/', views.site_table, name='site_table'),
    path('site_details/<int:site_id>', views.site_details, name='site_details'),
    path('site_create/', views.site_create, name='site_create'),
    path('sites/<int:site_id>', views.site_edit, name='site_edit'),
    path('sites/<int:site_id>/delete', views.site_delete, name='site_delete'),
    path('site_listgrid/<int:site_id>/', views.site_listgrid, name='site_listgrid'),
    path('site_nav/<int:site_id>/', views.site_nav, name='site_nav'),

    ### RACK ###
    path('racks/', views.racks, name='racks'),
    path('rack_table/', views.rack_table, name='rack_table'),
    path('rack_create/', views.rack_create, name='rack_create'),
    path('racks/<int:rack_id>', views.rack_detail, name='rack_detail'),
    path('racks/<int:rack_id>', views.rack_edit, name='rack_edit'),
    path('racks/<int:rack_id>/delete', views.rack_delete, name='rack_delete'),
    path('rack_nav/<int:rack_id>/', views.rack_nav, name='rack_nav'),

    ### VENDOR ###
    path('vendors/', views.vendors, name='vendors'),
    path('vendor_table/', views.vendor_table, name='vendor_table'),
    path('vendor_create/', views.vendor_create, name='vendor_create'),
    path('vendors/<int:vendor_id>', views.vendor_detail, name='vendor_detail'),
    path('vendors/<int:vendor_id>/delete', views.vendor_delete, name='vendor_delete'),
    path('vendor_nav/<int:vendor_id>/', views.vendor_nav, name='vendor_nav'),

    ### DEVICE ###
    path('devices/', views.devices, name='devices'),
    path('device_table/', views.device_table, name='device_table'),
    path('device_create/', views.device_create, name='device_create'),
    path('devices/<int:device_id>', views.device_detail, name='device_detail'),
    path('devices/<int:device_id>/delete', views.device_delete, name='device_delete'),
    path('device_nav/<int:device_id>/', views.device_nav, name='device_nav'),

    ### OPERATOR ###
    path('operators/', views.operators, name='operators'),
    path('operator_table/', views.operator_table, name='operator_table'),
    path('operator_create/', views.operator_create, name='operator_create'),
    path('operators/<int:operator_id>', views.operator_detail, name='operator_detail'),
    path('operators/<int:operator_id>/delete', views.operator_delete, name='operator_delete'),
    path('operator_nav/<int:operator_id>/', views.operator_nav, name='operator_nav'),
    
    ### CASE ###
    path('cases/', views.cases, name='cases'),
    path('case_table/', views.case_table, name='case_table'),
    path('case_create/', views.case_create, name='case_create'),
    path('cases/<int:case_id>', views.case_detail, name='case_detail'),
    path('cases/<int:case_id>/delete', views.case_delete, name='case_delete'),
    path('case_nav/<int:case_id>/', views.case_nav, name='case_nav'),
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)