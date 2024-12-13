from django.db import models

class JobPosting(models.Model):
    WORK_TYPE_CHOICES = [
        ("On-site", "On-site"),
        ("Hybrid", "Hybrid"),
    ]
    EMPLOYEE_TYPE_CHOICES = [
        ("Part-time", "Part-time"),
        ("Full-time", "Full-time"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES)
    employee_type = models.CharField(max_length=10, choices=EMPLOYEE_TYPE_CHOICES)
    offers = models.TextField()

    def __str__(self):
        return self.title


class CandidateScreening(models.Model):
    candidate = models.CharField(max_length=100)
    job_position = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name="candidates")
    members = models.TextField()
    conduct_interviews = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.candidate} - {self.job_position.title}"


class OnboardingProcess(models.Model):
    candidate = models.ForeignKey(CandidateScreening, on_delete=models.CASCADE, related_name="onboardings")
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    offer_letter = models.TextField()

    def __str__(self):
        return f"{self.candidate.candidate} - {self.designation}"