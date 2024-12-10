from django.db import models

"""Employee Table"""
class Employee(models.Model):
    # Personal Information
    title = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    nic = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    emergency_person = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=15)

    # Professional Information
    job_number = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.CharField(max_length=255, null=True, blank=True)
    immediate_supervisor = models.CharField(max_length=255)

    # Login Information
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)

    # Financial Information
    bank = models.CharField(max_length=255)
    account_number = models.BigIntegerField()
    account_holder = models.CharField(max_length=255)
    bank_code = models.IntegerField()
    branch_code = models.IntegerField()
    swift_code = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


"""Education Table"""
class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='educations')
    title = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.title} at {self.institute}"
    

"""Work History Table"""
class WorkHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='work_histories')
    position = models.CharField(max_length=100, default="Manager")
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company} ({self.start_date} - {self.end_date})"