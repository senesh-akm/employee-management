from django.shortcuts import render
from .models import SalaryProcessing, PayrollGeneration, TaxManagement

def salary_processing_list(request):
    salary_processings = SalaryProcessing.objects.all()
    return render(request, "salary_processing/salary_processing_list.html", {"salary_processings": salary_processings})

def payroll_generation_list(request):
    payroll_generation = PayrollGeneration.objects.all()
    return render(request, "payroll_generation/payroll_generation_list.html", {"payroll_generation": payroll_generation})

def tax_management_list(request):
    tax_management = TaxManagement.objects.all()
    return render(request, "tax_management/tax_management_list.html", {"tax_management": tax_management})