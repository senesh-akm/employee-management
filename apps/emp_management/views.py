from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from .models import Employee, Education, WorkHistory
from .forms import EmployeeForm, EducationForm, WorkHistoryForm
from django.forms import modelformset_factory

def add_employee(request):
    # Create formsets for Education and Work History
    EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1, can_delete=True)
    WorkHistoryFormSet = modelformset_factory(WorkHistory, form=WorkHistoryForm, extra=1, can_delete=True)

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        education_formset = EducationFormSet(request.POST, prefix="education")
        workhistory_formset = WorkHistoryFormSet(request.POST, prefix="workhistory")

        if form.is_valid() and education_formset.is_valid() and workhistory_formset.is_valid():
            employee = form.save()

            print("Saving education data...")
            for edu_form in education_formset:
                print(edu_form.cleaned_data)
                if edu_form.cleaned_data and not edu_form.cleaned_data.get("DELETE"):
                    edu_instance = edu_form.save(commit=False)
                    edu_instance.employee = employee
                    edu_instance.save()

            print("Saving work history data...")
            for work_form in workhistory_formset:
                print(work_form.cleaned_data) 
                if work_form.cleaned_data and not work_form.cleaned_data.get("DELETE"):
                    work_instance = work_form.save(commit=False)
                    work_instance.employee = employee
                    work_instance.save()

            return redirect("employee_list")
    else:
        form = EmployeeForm()
        education_formset = EducationFormSet(queryset=Education.objects.none(), prefix="education")
        workhistory_formset = WorkHistoryFormSet(queryset=WorkHistory.objects.none(), prefix="workhistory")

    # Define field groups for rendering
    personal_fields = ["title", "full_name", "dob", "nic", "address", "contact_number", "email", "emergency_person", "emergency_contact"]
    professional_fields = ["job_number", "job_title", "department", "designation", "date_of_joining", "salary", "skills", "immediate_supervisor"]
    login_fields = ["username", "password"]
    financial_fields = ["bank", "account_number", "account_holder", "bank_code", "branch_code", "swift_code"]

    context = {
        "form": form,
        "education_formset": education_formset,
        "workhistory_formset": workhistory_formset,
        "personal_fields": personal_fields,
        "professional_fields": professional_fields,
        "login_fields": login_fields,
        "financial_fields": financial_fields,
    }

    print(get_template('base.html'))
    return render(request, "employee/add_employee.html", context)

def employee_list(request):
    print(get_template('base.html'))
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employees": employees})

def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    educations = employee.educations.all()
    work_histories = employee.work_histories.all()

    if request.method == "POST":
        try:
            employee.dob = datetime.strptime(request.POST.get("dob"), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            employee.dob = None  # Handle invalid or blank dates gracefully

        try:
            employee.date_of_joining = datetime.strptime(request.POST.get("date_of_joining"), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            employee.date_of_joining = None

        # Update other fields...
        employee.title = request.POST.get("title")
        employee.full_name = request.POST.get("full_name")
        employee.nic = request.POST.get("nic")
        employee.address = request.POST.get("address")
        employee.contact_number = request.POST.get("contact_number")
        employee.email = request.POST.get("email")
        employee.emergency_person = request.POST.get("emergency_person")
        employee.emergency_contact = request.POST.get("emergency_contact")
        employee.job_number = request.POST.get("job_number")
        employee.job_title = request.POST.get("job_title")
        employee.department = request.POST.get("department")
        employee.designation = request.POST.get("designation")
        employee.salary = request.POST.get("salary")
        employee.skills = request.POST.get("skills")
        employee.immediate_supervisor = request.POST.get("immediate_supervisor")
        employee.username = request.POST.get("username")
        employee.password = request.POST.get("password")
        employee.bank = request.POST.get("bank")
        employee.account_number = request.POST.get("account_number")
        employee.account_holder = request.POST.get("account_holder")
        employee.bank_code = request.POST.get("bank_code")
        employee.branch_code = request.POST.get("branch_code")
        employee.swift_code = request.POST.get("swift_code")

        # Save the employee record
        employee.save()
        return redirect("employee_list")

    print(get_template('base.html'))
    return render(request, "employee/employee_details.html", {
        "employee": employee,
        "educations": educations,
        "work_histories": work_histories
    })