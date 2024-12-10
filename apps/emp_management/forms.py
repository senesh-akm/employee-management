from django import forms
from .models import Employee, Education, WorkHistory

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'dob': forms.DateInput(attrs={'class': 'form-control w-100', 'type': 'date'}),
            'nic': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'address': forms.Textarea(attrs={'class': 'form-control w-100', 'rows': 3}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'email': forms.EmailInput(attrs={'class': 'form-control w-100'}),
            'emergency_person': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'job_number': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'department': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'designation': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'date_of_joining': forms.DateInput(attrs={'class': 'form-control w-100', 'type': 'date'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'skills': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'immediate_supervisor': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'username': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control w-100'}),
            'resume': forms.FileInput(attrs={'class': 'form-control w-100'}),
            'nic_front': forms.FileInput(attrs={'class': 'form-control w-100'}),
            'nic_back': forms.FileInput(attrs={'class': 'form-control w-100'}),
            'passport': forms.FileInput(attrs={'class': 'form-control w-100'}),
            'service_letter': forms.FileInput(attrs={'class': 'form-control w-100'}),
            'certificate_of_grama_niladhari': forms.FileInput(attrs={'class': 'form-control w-100'}),
            'bank': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'account_number': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'account_holder': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'bank_code': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'branch_code': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'swift_code': forms.TextInput(attrs={'class': 'form-control w-100'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["title", "institute", "start_date", "end_date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control w-100"}),
            "institute": forms.TextInput(attrs={"class": "form-control w-100"}),
            "start_date": forms.DateInput(attrs={"class": "form-control w-100", "type": "date"}),
            "end_date": forms.DateInput(attrs={"class": "form-control w-100", "type": "date"}),
        }

class WorkHistoryForm(forms.ModelForm):
    class Meta:
        model = WorkHistory
        fields = ["position", "company", "start_date", "end_date"]
        widgets = {
            "position": forms.TextInput(attrs={"class": "form-control w-100"}),
            "company": forms.TextInput(attrs={"class": "form-control w-100"}),
            "start_date": forms.DateInput(attrs={"class": "form-control w-100", "type": "date"}),
            "end_date": forms.DateInput(attrs={"class": "form-control w-100", "type": "date"}),
        }
