from django.urls import path
from . import views

urlpatterns = [
    path("training-needs/", views.need_trainings_list, name="need_trainings_list"),
    path("training-needs/add/", views.add_need_training, name="add_training_need"),
    path("training-needs/edit/<int:training_need_id>/", views.need_details, name="need_details"),
    # path("training-needs/salary/<int:employee_id>", views.get_emp_desgination, name="get_emp_desgination"),

    path("training-plans/", views.training_plans_list, name="training_plans_list"),
    path("training-plans/add/", views.add_training_plan, name="add_training_plan"),
    path("training-plans/edit/<int:plan_id>", views.training_plan_view, name="training_plan_view"),

    path("training-records/", views.training_record_list, name="training_record_list"),
    path("training-records/add/", views.add_training_record, name="add_training_record"),
    path("training-records/edit/<int:record_id>", views.training_record_details, name="training_record_details"),
]