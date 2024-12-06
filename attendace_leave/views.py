from django.shortcuts import render, get_object_or_404
from .models import Attendance, Leave

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_leave/attendance_list.html', {'attendances': attendances})


def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'attendance_leave/leave_list.html', {'leaves': leaves})