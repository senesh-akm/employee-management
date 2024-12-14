from django.db import models
from apps.emp_management.models import Employee

class ExitInterview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="exit_interviews")
    stars = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return f"Exit Interview - {self.employee.full_name}"


class FinalSettlement(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="final_settlements")
    settlement_clearance = models.CharField(max_length=255)

    def __str__(self):
        return f"Final Settlement - {self.employee.full_name}"


class RecordKeeping(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="record_keeping")
    final_records = models.TextField()
    exit_letter = models.TextField()
    service_letter = models.TextField()

    def __str__(self):
        return f"Record Keeping - {self.employee.full_name}"