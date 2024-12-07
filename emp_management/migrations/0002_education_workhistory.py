# Generated by Django 5.1.3 on 2024-12-03 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('institute', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='emp_management.employee')),
            ],
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_histories', to='emp_management.employee')),
            ],
        ),
    ]