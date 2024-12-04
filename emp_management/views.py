from django.shortcuts import render, get_object_or_404, redirect
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
            # Save the Employee instance
            employee = form.save()

            # Save each Education instance linked to this Employee
            for edu_form in education_formset:
                if edu_form.cleaned_data and not edu_form.cleaned_data.get("DELETE"):
                    edu_instance = edu_form.save(commit=False)
                    edu_instance.employee = employee
                    edu_instance.save()

            # Save each Work History instance linked to this Employee
            for work_form in workhistory_formset:
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

    return render(request, "employee/add_employee.html", context)

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employees": employees})

def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "employee/employee_details.html", {"employee": employee})