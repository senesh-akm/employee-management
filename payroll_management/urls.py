from django.urls import path
from . import views

urlpatterns = [
    path("salary-processing/", views.salary_processing_list, name="salary_processing_list"),
    # path("salary-processing/add/", views.add_salary_processing, name="add_salary_processing"),

    path("payroll/", views.payroll_generation_list, name="payroll_list"),
    # path("payroll/add/", views.add_payroll, name="add_payroll"),

    path("tax-management/", views.tax_management_list, name="tax_management_list"),
    # path("tax-management/add/", views.add_tax_management, name="add_tax_management"),
]