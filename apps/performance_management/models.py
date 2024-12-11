from django.db import models
from apps.emp_management.models import Employee

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="performance_reviews")
    review_text = models.TextField()
    appraisal_text = models.TextField()

    def __str__(self):
        return f"Performance Review for {self.employee.full_name}"


class GoalSetting(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="goal_settings")
    goals = models.TextField()

    def __str__(self):
        return f"Goals for {self.employee.full_name}"


class FeedbackMechanism(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="feedbacks")
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.employee.full_name}"