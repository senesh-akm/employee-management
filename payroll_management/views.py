from django.shortcuts import render, redirect, get_object_or_404
from .models import SalaryProcessing, PayrollGeneration, TaxManagement
from emp_management.models import Employee
from django.http import JsonResponse

def salary_processing_list(request):
    salary_processings = SalaryProcessing.objects.all()
    return render(request, "salary_processing/salary_processing_list.html", {"salary_processings": salary_processings})


def add_salary_processing(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        salary = request.POST.get("salary")
        deduction = request.POST.get("deduction")
        taxes = request.POST.get("taxes")
        no_pay = request.POST.get("no_pay")
        days = request.POST.get("days")
        payment = request.POST.get("payment")
        status = request.POST.get("status") == "True"

        employee = get_object_or_404(Employee, pk=employee_id)

        SalaryProcessing.objects.create(
            employee=employee,
            salary=salary,
            deduction=deduction,
            taxes=taxes,
            no_pay=no_pay,
            days=days,
            payment=payment,
            status=status,
        )
        return redirect("salary_processing_list")

    employees = Employee.objects.all()
    return render(request, "salary_processing/add_salary_processing.html", {"employees": employees})


def get_bank_details(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        bank_details = {
            "bank": employee.bank,
            "account_number": employee.account_number,
            "account_holder": employee.account_holder,
            "bank_code": employee.bank_code,
            "branch_code": employee.branch_code,
            "swift_code": employee.swift_code,
            "salary": employee.salary,
        }
        return JsonResponse({"success": True, "bank_details": bank_details})
    except Employee.DoesNotExist:
        return JsonResponse({"success": False, "error": "Employee not found"})


def salary_details(request, pk):
    salary_processing = get_object_or_404(SalaryProcessing, pk=pk)
    employees = Employee.objects.all()

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        salary = request.POST.get("salary")
        deduction = request.POST.get("deduction")
        taxes = request.POST.get("taxes")
        no_pay = request.POST.get("no_pay")
        days = request.POST.get("days")
        payment = request.POST.get("payment")
        status = request.POST.get("status") == "True"

        salary_processing.employee = get_object_or_404(Employee, pk=employee_id)
        salary_processing.salary = salary
        salary_processing.deduction = deduction
        salary_processing.taxes = taxes
        salary_processing.no_pay = no_pay
        salary_processing.days = days
        salary_processing.payment = payment
        salary_processing.status = status
        salary_processing.save()

        return redirect("salary_processing_list")

    return render(request, "salary_processing/salary_details.html", {
        "salary_processing": salary_processing,
        "employees": employees,
    })


def payroll_generation_list(request):
    payroll_generation = PayrollGeneration.objects.all()
    return render(request, "payroll_generation/payroll_generation_list.html", {"payroll_generation": payroll_generation})


def tax_management_list(request):
    tax_management = TaxManagement.objects.all()
    return render(request, "tax_management/tax_management_list.html", {"tax_management": tax_management})


def add_tax_management(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        income_tax = request.POST.get("income_tax")
        social_security = request.POST.get("social_security")
        other_taxes = request.POST.get("other_taxes")

        employee = get_object_or_404(Employee, pk=employee_id)

        TaxManagement.objects.create(
            employee=employee,
            income_tax=income_tax,
            social_security=social_security,
            other_taxes=other_taxes,
        )
        return redirect("tax_management_list")

    employees = Employee.objects.all()
    return render(request, "tax_management/add_tax_management.html", {"employees": employees})


def get_salary(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        salary = {
            "salary": employee.salary,
        }
        return JsonResponse({"success": True, "salary": salary})
    except Employee.DoesNotExist:
        return JsonResponse({"success": False, "error": "Employee not found"})


def tax_details(request, pk):
    tax_management = get_object_or_404(SalaryProcessing, pk=pk)
    employees = Employee.objects.all()

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        income_tax = request.POST.get("income_tax")
        social_security = request.POST.get("social_security")
        other_taxes = request.POST.get("other_taxes")

        tax_management.employee = get_object_or_404(Employee, pk=employee_id)
        tax_management.income_tax = income_tax
        tax_management.social_security = social_security
        tax_management.other_taxes = other_taxes
        tax_management.save()

        return redirect("tax_management")

    return render(request, "tax_management/tax_details.html", {
        "tax_management": tax_management,
        "employees": employees,
    })