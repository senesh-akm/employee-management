from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance, Leave
from apps.emp_management.models import Employee

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_leave/attendance/attendance_list.html', {'attendances': attendances})


def add_leave(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        leave_type = request.POST.get("leave_type")
        leave_count = request.POST.get("leave_count")
        used_leave = request.POST.get("used_leave")
        leave_balance = request.POST.get("leave_balance")
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")
        approval_status = request.POST.get("approval_status")
        reason = request.POST.get("reason")

        employee = get_object_or_404(Employee, id=employee_id)

        Leave.objects.create(
            employee=employee,
            leave_type=leave_type,
            leave_count=leave_count,
            used_leave=used_leave,
            leave_balance=leave_balance,
            from_date=from_date,
            to_date=to_date,
            approval_status=approval_status,
            reason=reason,
        )

        return redirect("leave_list")
    else:
        employees = Employee.objects.all()
        return render(request, "attendance_leave/leave/add_leave.html", {"employees": employees})


def leave_details(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if request.method == "POST":
        print("Form Data:", request.POST)

        try:
            employee_id = request.POST.get("employee")
            leave.employee = get_object_or_404(Employee, pk=employee_id)

            leave.leave_type = request.POST.get("leave_type")
            leave.leave_count = int(request.POST.get("leave_count") or 0)
            leave.used_leave = int(request.POST.get("used_leave") or 0)
            leave.leave_balance = int(request.POST.get("leave_balance") or 0)

            leave.from_date = datetime.strptime(request.POST.get("from_date"), "%Y-%m-%d").date()
            leave.to_date = datetime.strptime(request.POST.get("to_date"), "%Y-%m-%d").date()

            leave.approval_status = request.POST.get("approval_status")
            leave.reason = request.POST.get("reason")

            leave.save()
            return redirect("leave_list")
        except ValueError as e:
            print("Error:", e)
            return render(request, "attendance_leave/leave/leave_details.html", {
                "leave": leave,
                "employees": Employee.objects.all(),
                "error_message": "Invalid input. Please check all fields and try again.",
            })

    employees = Employee.objects.all()
    return render(request, "attendance_leave/leave/leave_details.html", {
        "leave": leave,
        "employees": employees,
    })


def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'attendance_leave/leave/leave_list.html', {'leaves': leaves})