from django.urls import path

from . import views

urlpatterns = [
    # path("", views.add_employee, name="index"),
    path("", views.employee_list, name='employee_list'),
    path("add/", views.add_employee, name='add_employee'),
    path("<int:pk>/", views.employee_details, name='employee_details'),
]