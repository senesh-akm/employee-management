from django.urls import path
from . import views

urlpatterns = [
    path("exit-interviews/", views.exit_interview_list, name="exit_interview_list"),
    path("exit-interviews/add/", views.add_exit_interview, name="add_exit_interview"),
    path("exit-interviews/edit/<int:interview_id>/", views.edit_exit_interview, name="edit_exit_interview"),

    path("final-settlements/", views.final_settlement_list, name="final_settlement_list"),
    path("final-settlements/add/", views.add_final_settlement, name="add_final_settlement"),
    path("final-settlements/edit/<int:settlement_id>/", views.edit_final_settlement, name="edit_final_settlement"),

    path("record-keeping/", views.record_keeping_list, name="record_keeping_list"),
    path("record-keeping/add/", views.add_record_keeping, name="add_record_keeping"),
    path("record-keeping/edit/<int:record_id>/", views.edit_record_keeping, name="edit_record_keeping"),
]