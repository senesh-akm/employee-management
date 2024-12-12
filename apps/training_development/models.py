from django.db import models
from apps.emp_management.models import Employee

class TrainingNeedsAssessment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="training_needs")
    designation = models.CharField(max_length=100)
    DURATION_CHOICES = [
        ("1 month", "1 month"),
        ("2 months", "2 months"),
        ("3 months", "3 months"),
        ("6 months", "6 months"),
        ("over 6 months", "Over 6 months"),
    ]
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)

    def __str__(self):
        return f"{self.employee.full_name} - {self.designation}"
    

class TrainingPlan(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="training_plans")
    plan = models.TextField()

    def __str__(self):
        return f"Training Plan for {self.employee.full_name}"
    

class TrainingRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="training_records")
    MONTH_CHOICES = [(str(i), str(i)) for i in range(1, 13)]
    month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    TRAINING_RECORD_CHOICES = [(i, str(i)) for i in range(1, 6)]
    training_record = models.IntegerField(choices=TRAINING_RECORD_CHOICES)
    description = models.TextField()
    certificate = models.BooleanField(default=False)

    def __str__(self):
        return f"Training Record for {self.employee.full_name} - Month {self.month}"