from django.db import models
from emp_management.models import Employee

"""Employee Attendance"""
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    work_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    overtime = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Absent')

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"
    

"""Employee Leave"""
class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="leaves")
    LEAVE_TYPE_CHOICES = [
        ('Casual Leave', 'Casual Leave'),
        ('Annual Leave', 'Annual Leave'),
        ('Short Leave', 'Short Leave'),
    ]
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    leave_count = models.PositiveIntegerField()
    used_leave = models.PositiveIntegerField(default=0)
    leave_balance = models.PositiveIntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    APPROVAL_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Cancelled', 'Cancelled'),
    ]
    approval_status = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.employee.full_name} - {self.leave_type} ({self.from_date} to {self.to_date})"