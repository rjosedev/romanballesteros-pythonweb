# Generated by Django 5.0.6 on 2024-07-05 16:55

import django.db.models.deletion
import smart_selects.db_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userImage', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryId', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('categoryId', 'name'),
                'unique_together': {('categoryId', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operatorId', models.CharField(max_length=6)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('backOffice', models.CharField(max_length=20)),
                ('operatorImage', models.ImageField(blank=True, default='/media/static/default.png', null=True, upload_to='operators')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Operator',
                'verbose_name_plural': 'Operators',
                'ordering': ('operatorId', 'firstName', 'lastName'),
                'unique_together': {('operatorId', 'firstName', 'lastName')},
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteId', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('switchowner', models.CharField(max_length=30)),
                ('contact', models.IntegerField(default=0)),
                ('siteImage', models.ImageField(blank=True, default='/media/static/default.png', null=True, upload_to='sites')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
                'ordering': ('siteId', 'name'),
                'unique_together': {('siteId', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rackId', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=20)),
                ('rackImage', models.ImageField(blank=True, default='/media/static/default.png', null=True, upload_to='racks')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.site')),
            ],
            options={
                'verbose_name': 'Rack',
                'verbose_name_plural': 'Racks',
                'ordering': ('rackId', 'name'),
                'unique_together': {('rackId', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorId', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('link', models.URLField(blank=True)),
                ('vendorImage', models.ImageField(blank=True, default='/media/static/default.png', null=True, upload_to='vendors')),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendors',
                'ordering': ('vendorId', 'name'),
                'unique_together': {('vendorId', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('RT', 'Router'), ('SW2', 'Switch L2'), ('SW3', 'Switch L3'), ('FW', 'Firewall'), ('SR', 'Server'), ('ST', 'Storage')], max_length=3, null=True)),
                ('model', models.CharField(max_length=20)),
                ('serialNumber', models.CharField(max_length=30)),
                ('deviceImage', models.ImageField(blank=True, default='/media/static/default.png', null=True, upload_to='devices')),
                ('rack', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='site', chained_model_field='site', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='tasks.rack')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.site')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.vendor')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': ('deviceId', 'name'),
                'unique_together': {('deviceId', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseId', models.CharField(max_length=6)),
                ('description', models.CharField(max_length=20)),
                ('severity', models.CharField(choices=[('1', '1. Not classified'), ('2', '2. Information'), ('3', '3. Warning'), ('4', '4. Average'), ('5', '5. High'), ('6', '6. Disaster')], max_length=2, null=True)),
                ('caseImage', models.ImageField(blank=True, default='/media/static/default.png', null=True, upload_to='cases')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.device')),
                ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.operator')),
                ('rack', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.rack')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.site')),
                ('vendor', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.vendor')),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
                'ordering': ('caseId', 'description'),
                'unique_together': {('caseId', 'description')},
            },
        ),
    ]
