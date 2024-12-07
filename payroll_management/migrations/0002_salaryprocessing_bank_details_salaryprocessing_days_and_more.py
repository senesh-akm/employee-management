# Generated by Django 5.1.3 on 2024-12-07 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_management', '0005_alter_employee_skills'),
        ('payroll_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryprocessing',
            name='bank_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_details', to='emp_management.employee'),
        ),
        migrations.AddField(
            model_name='salaryprocessing',
            name='days',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salaryprocessing',
            name='no_pay',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
