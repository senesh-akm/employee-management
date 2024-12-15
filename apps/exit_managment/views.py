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


def final_settlement_list(request):
    final_settlements = FinalSettlement.objects.all()
    return render(request, "final_settlement/final_settlement_list.html", {"final_settlements": final_settlements})


def add_final_settlement(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        settlement_clearance = request.POST.get("settlement_clearance")
        employee = get_object_or_404(Employee, pk=employee_id)
        FinalSettlement.objects.create(employee=employee, settlement_clearance=settlement_clearance)
        return redirect("final_settlement_list")

    employees = Employee.objects.all()
    return render(request, "final_settlement/add_final_settlement.html", {"employees": employees})


def edit_final_settlement(request, settlement_id):
    settlement = get_object_or_404(FinalSettlement, pk=settlement_id)

    if request.method == "POST":
        settlement.settlement_clearance = request.POST.get("settlement_clearance")
        settlement.save()
        return redirect("final_settlement_list")

    return render(request, "final_settlement/edit_final_settlement.html", {"settlement": settlement})


def record_keeping_list(request):
    record_keeping = RecordKeeping.objects.all()
    return render(request, "record_keeping/record_keeping_list.html", {"record_keeping": record_keeping})


def add_record_keeping(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        final_records = request.POST.get("final_records")
        exit_letter = request.POST.get("exit_letter")
        service_letter = request.POST.get("service_letter")

        employee = get_object_or_404(Employee, pk=employee_id)
        RecordKeeping.objects.create(
            employee=employee,
            final_records=final_records,
            exit_letter=exit_letter,
            service_letter=service_letter,
        )
        return redirect("record_keeping_list")

    employees = Employee.objects.all()
    return render(request, "record_keeping/add_record_keeping.html", {"employees": employees})


def edit_record_keeping(request, record_id):
    record = get_object_or_404(RecordKeeping, pk=record_id)

    if request.method == "POST":
        record.final_records = request.POST.get("final_records")
        record.exit_letter = request.POST.get("exit_letter")
        record.service_letter = request.POST.get("service_letter")
        record.save()
        return redirect("record_keeping_list")

    return render(request, "record_keeping/edit_record_keeping.html", {"record": record})