# Generated by Django 5.0.6 on 2024-06-22 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='caseClosed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='caseCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
