from django.urls import path
from . import views

urlpatterns = [
    path("salary-processing/", views.salary_processing_list, name="salary_processing_list"),
    path("salary-processing/add/", views.add_salary_processing, name="add_salary_processing"),
    path("salary-processing/<int:pk>/", views.salary_details, name='salary_details'),
    path("salary-processing/bank-details/<int:employee_id>/", views.get_bank_details, name="get_bank_details"),

    path("payroll/", views.payroll_generation_list, name="payroll_list"),
    # path("payroll/add/", views.add_payroll, name="add_payroll"),

    path("tax-management/", views.tax_management_list, name="tax_management_list"),
    path("tax-management/add/", views.add_tax_management, name="add_tax_management"),
    path("tax-management/<int:pk>/", views.tax_details, name='tax_details'),
    path("tax-management/salary/<int:employee_id>/", views.get_salary, name="get_salary"),
]