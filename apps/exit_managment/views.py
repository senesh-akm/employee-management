from django.shortcuts import render, redirect, get_object_or_404
from .models import ExitInterview, FinalSettlement, RecordKeeping
from apps.emp_management.models import Employee


def exit_interview_list(request):
    interviews = ExitInterview.objects.all()
    return render(request, "exit_interview/exit_interview_list.html", {"interviews": interviews})


def add_exit_interview(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        stars = request.POST.get("stars")
        feedback = request.POST.get("feedback")
        employee = get_object_or_404(Employee, pk=employee_id)

        ExitInterview.objects.create(employee=employee, stars=stars, feedback=feedback)
        return redirect("exit_interview_list")

    employees = Employee.objects.all()
    return render(request, "exit_interview/add_exit_interview.html", {"employees": employees})


def edit_exit_interview(request, interview_id):
    interview = get_object_or_404(ExitInterview, pk=interview_id)

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        stars = request.POST.get("stars")
        feedback = request.POST.get("feedback")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            interview.employee = employee
            interview.stars = stars
            interview.feedback = feedback
            interview.save()
            return redirect("exit_interview_list")
        except Employee.DoesNotExist:
            return render(request, "exit_interview/edit_exit_interview.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all(),
                "interview": interview,
            })

    employees = Employee.objects.all()
    return render(request, "exit_interview/edit_exit_interview.html", {
        "employees": employees,
        "interview": interview,
    })
