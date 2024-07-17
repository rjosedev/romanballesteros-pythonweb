from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task, Site, Rack, Vendor, Device, Operator, Case, Avatar
from .forms import TaskForm, SiteForm, SiteEditForm, RackForm, VendorForm, DeviceForm, OperatorForm, CaseForm, UserEditForm

# Create your views here.




### MAIN: Home, Pages, About ###

def home(request):
    return render(request, 'home.html')

def pages(request):
    return render(request, 'pages.html')

def about(request):
    return render(request, 'about.html')

def only_staff(request):
    return render(request, 'only_staff.html')




### USER: Sing In, Sign Up, Edit profile, Logout ###

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"],
                    password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

@login_required
def profile_detail(request):
    return render(request, 'profile_detail.html')

@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.set_password(data['password2'])
            user.save()
            return render(request, 'profile_edit.html', {"message": "User profile successfully updated."})
        else:
            return render(request, 'profile_edit.html', {"form": form})
    else:
        form = UserEditForm(instance=request.user)
        return render(request, 'profile_edit.html', {"form": form})

@login_required
def signout(request):
    logout(request)
    return redirect('home')




### SITE: Create, List, Table, Scroll, List/Grid, Nav, Edit/Delete ###

@staff_member_required(login_url='/only_staff')
def site_create(request):
    if request.method == "GET":
        return render(request, 'site_create.html', {"form": SiteForm})
    else:
        try:
            form = SiteForm(request.POST, request.FILES)
            new_site = form.save(commit=False)
            new_site.user = request.user
            new_site.save()

            return redirect('sites')
        except ValueError:
            return render(request, 'site_create.html', {"form": SiteForm, "error": "Error creating site."})

@login_required
def sites(request):
    sites = Site.objects.filter()
    return render(request, 'sites.html', {"sites": sites})

@login_required
def site_table(request):
    sites = Site.objects.all()
    return render(request, 'site_table.html', {'sites': sites})

@login_required
def site_scroll(request):
    sites = Site.objects.filter()
    return render(request, 'site_scroll.html', {"sites": sites})

@login_required
def site_nav(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    sites = Site.objects.all()
    return render(request, 'site_nav.html', {'site': site, 'sites': sites})

@login_required
def site_listgrid(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    sites = Site.objects.all()
    return render(request, 'site_listgrid.html', {'site': site, 'sites': sites})

@login_required
def site_details(request, site_id):
    site = Site.objects.get(pk=site_id)
    template = loader.get_template('site_details.html')
    context = {
      'site': site,
    }
    return HttpResponse(template.render(context, request))

@staff_member_required(login_url='/only_staff')
def site_edit(request, site_id):
    if request.method == 'GET':
        site = get_object_or_404(Site, pk=site_id)
        form = SiteForm(instance=site)
        return render(request, 'site_edit.html', {'site': site, 'form': form})
    else:
        try:
            site = get_object_or_404(Site, pk=site_id)
            form = SiteForm(request.POST, request.FILES, instance=site)
            form.save()

            return redirect('sites')
        except ValueError:
            return render(request, 'site_edit.html', {'site': site, 'form': form, 'error': 'Error updating site.'})

@staff_member_required(login_url='/only_staff')
def site_delete(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        site.delete()
        return redirect('sites')




### RACK: Create, List, Table, Nav, Edit/Delete ###

@staff_member_required(login_url='/only_staff')
def rack_create(request):
    if request.method == "GET":
        return render(request, 'rack_create.html', {"form": RackForm})
    else:
        try:
            form = RackForm(request.POST, request.FILES)
            new_rack = form.save(commit=False)
            new_rack.user = request.user
            new_rack.save()
            return redirect('racks')
        except ValueError:
            return render(request, 'rack_create.html', {"form": RackForm, "error": "Error creating rack."})

@login_required
def racks(request):
    racks = Rack.objects.filter()
    return render(request, 'racks.html', {"racks": racks})

@login_required
def rack_table(request):
    racks = Rack.objects.all()
    return render(request, 'rack_table.html', {'racks': racks})

@login_required
def rack_nav(request, rack_id):
    rack = get_object_or_404(Rack, id=rack_id)
    racks = Rack.objects.all()
    return render(request, 'rack_nav.html', {'rack': rack, 'racks': racks})

@staff_member_required(login_url='/only_staff')
def rack_detail(request, rack_id):
    if request.method == 'GET':
        rack = get_object_or_404(Rack, pk=rack_id)
        form = RackForm(instance=rack)
        return render(request, 'rack_detail.html', {'rack': rack, 'form': form})
    else:
        try:
            rack = get_object_or_404(Rack, pk=rack_id)
            form = RackForm(request.POST, request.FILES, instance=rack)
            form.save()

            return redirect('racks')
        except ValueError:
            return render(request, 'rack_detail.html', {'rack': rack, 'form': form, 'error': 'Error updating rack.'})

@staff_member_required(login_url='/only_staff')
def rack_edit(request, rack_id):
    if request.method == 'GET':
        rack = get_object_or_404(Rack, pk=rack_id)
        form = RackForm(instance=rack)
        return render(request, 'rack_edit.html', {'rack': rack, 'form': form})
    else:
        try:
            rack = get_object_or_404(Rack, pk=rack_id)
            form = RackForm(request.POST, request.FILES, instance=rack)
            form.save()

            return redirect('racks')
        except ValueError:
            return render(request, 'rack_edit.html', {'rack': rack, 'form': form, 'error': 'Error updating rack.'})

@staff_member_required(login_url='/only_staff')
def rack_delete(request, rack_id):
    rack = get_object_or_404(Rack, pk=rack_id)
    if request.method == 'POST':
        rack.delete()
        return redirect('racks')





### VENDOR: Create, List, Table, Nav, Edit/Delete ###

@staff_member_required(login_url='/only_staff')
def vendor_create(request):
    if request.method == "GET":
        return render(request, 'vendor_create.html', {"form": VendorForm})
    else:
        try:
            form = VendorForm(request.POST, request.FILES)
            new_vendor = form.save(commit=False)
            new_vendor.user = request.user
            new_vendor.save()
            return redirect('vendors')
        except ValueError:
            return render(request, 'vendor_create.html', {"form": VendorForm, "error": "Error creating vendor."})

@login_required
def vendors(request):
    vendors = Vendor.objects.filter()
    return render(request, 'vendors.html', {"vendors": vendors})

@login_required
def vendor_table(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_table.html', {'vendors': vendors})

@login_required
def vendor_nav(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    vendors = Vendor.objects.all()
    return render(request, 'vendor_nav.html', {'vendor': vendor, 'vendors': vendors})

@staff_member_required(login_url='/only_staff')
def vendor_detail(request, vendor_id):
    if request.method == 'GET':
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        form = VendorForm(instance=vendor)
        return render(request, 'vendor_detail.html', {'vendor': vendor, 'form': form})
    else:
        try:
            vendor = get_object_or_404(Vendor, pk=vendor_id)
            form = VendorForm(request.POST, request.FILES, instance=vendor)
            form.save()
            return redirect('vendors')
        except ValueError:
            return render(request, 'vendor_detail.html', {'vendor': vendor, 'form': form, 'error': 'Error updating vendor.'})

@staff_member_required(login_url='/only_staff')
def vendor_delete(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendors')




### DEVICE: Create, List, Table, Nav, Edit/Delete ###

@staff_member_required(login_url='/only_staff')
def device_create(request):
    if request.method == "GET":
        return render(request, 'device_create.html', {"form": DeviceForm})
    else:
        try:
            form = DeviceForm(request.POST, request.FILES)
            new_device = form.save(commit=False)
            new_device.user = request.user
            new_device.save()
            return redirect('devices')
        except ValueError:
            return render(request, 'device_create.html', {"form": DeviceForm, "error": "Error creating device."})

@login_required
def devices(request):
    devices = Device.objects.filter()
    return render(request, 'devices.html', {"devices": devices})

@login_required
def device_table(request):
    devices = Device.objects.all()
    return render(request, 'device_table.html', {'devices': devices})

@login_required
def device_nav(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    devices = Device.objects.all()
    return render(request, 'device_nav.html', {'device': device, 'devices': devices})

@staff_member_required(login_url='/only_staff')
def device_detail(request, device_id):
    if request.method == 'GET':
        device = get_object_or_404(Device, pk=device_id)
        form = DeviceForm(instance=device)
        return render(request, 'device_detail.html', {'device': device, 'form': form})
    else:
        try:
            device = get_object_or_404(Device, pk=device_id)
            form = DeviceForm(request.POST, request.FILES, instance=device)
            form.save()
            return redirect('devices')
        except ValueError:
            return render(request, 'device_detail.html', {'device': device, 'form': form, 'error': 'Error updating device.'})

@staff_member_required(login_url='/only_staff')
def device_delete(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST':
        device.delete()
        return redirect('devices')




### OPERATOR: Create, List, Table, Nav, Edit/Delete ###

@staff_member_required(login_url='/only_staff')
def operator_create(request):
    if request.method == "GET":
        return render(request, 'operator_create.html', {"form": OperatorForm})
    else:
        try:
            form = OperatorForm(request.POST, request.FILES)
            new_operator = form.save(commit=False)
            new_operator.user = request.user
            new_operator.save()
            return redirect('operators')
        except ValueError:
            return render(request, 'operator_create.html', {"form": OperatorForm, "error": "Error creating operator."})

@login_required
def operators(request):
    operators = Operator.objects.filter()
    return render(request, 'operators.html', {"operators": operators})

@login_required
def operator_table(request):
    operators = Operator.objects.all()
    return render(request, 'operator_table.html', {'operators': operators})

@login_required
def operator_nav(request, operator_id):
    operator = get_object_or_404(Operator, id=operator_id)
    operators = Operator.objects.all()
    return render(request, 'operator_nav.html', {'operator': operator, 'operators': operators})

@staff_member_required(login_url='/only_staff')
def operator_detail(request, operator_id):
    if request.method == 'GET':
        operator = get_object_or_404(Operator, pk=operator_id)
        form = OperatorForm(instance=operator)
        return render(request, 'operator_detail.html', {'operator': operator, 'form': form})
    else:
        try:
            operator = get_object_or_404(Operator, pk=operator_id)
            form = OperatorForm(request.POST, request.FILES, instance=operator)
            form.save()
            return redirect('operators')
        except ValueError:
            return render(request, 'operator_detail.html', {'operator': operator, 'form': form, 'error': 'Error updating operator.'})

@staff_member_required(login_url='/only_staff')
def operator_delete(request, operator_id):
    operator = get_object_or_404(Operator, pk=operator_id)
    if request.method == 'POST':
        operator.delete()
        return redirect('operators')




### CASE: Create, List, Table, Nav, Edit/Delete ###

@login_required
def case_create(request):
    if request.method == "GET":
        return render(request, 'case_create.html', {"form": CaseForm})
    else:
        try:
            form = CaseForm(request.POST, request.FILES)
            new_case = form.save(commit=False)
            new_case.user = request.user
            new_case.save()
            return redirect('cases')
        except ValueError:
            return render(request, 'case_create.html', {"form": CaseForm, "error": "Error creating case."})

@login_required
def cases(request):
    cases = Case.objects.filter()
    return render(request, 'cases.html', {"cases": cases})

@login_required
def case_table(request):
    cases = Case.objects.all()
    return render(request, 'case_table.html', {'cases': cases})

@login_required
def case_nav(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    cases = Case.objects.all()
    return render(request, 'case_nav.html', {'case': case, 'cases': cases})

@login_required
def case_detail(request, case_id):
    if request.method == 'GET':
        case = get_object_or_404(Case, pk=case_id)
        form = CaseForm(instance=case)
        return render(request, 'case_detail.html', {'case': case, 'form': form})
    else:
        try:
            case = get_object_or_404(Case, pk=case_id)
            form = CaseForm(request.POST, request.FILES, instance=case)
            form.save()
            return redirect('cases')
        except ValueError:
            return render(request, 'case_detail.html', {'case': case, 'form': form, 'error': 'Error updating case.'})

@login_required
def case_delete(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        case.delete()
        return redirect('cases')




### TASK:  Create, List pending, List completed, Table, Edit/Delete ###

@login_required
def task_create(request):
    if request.method == "GET":
        return render(request, 'task_create.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_create.html', {"form": TaskForm, "error": "Error creating task."})

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, completed__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def task_table(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_table.html', {'tasks': tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, completed__isnull=False).order_by('-completed')
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})

@login_required
def task_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.completed = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')