from django.urls import path
from . import views

urlpatterns = [
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('leave/', views.leave_list, name='leave_list'),
    path('leave/add/', views.add_leave, name='add_leave'),
    path("leave/<int:pk>/", views.leave_details, name='leave_details'),
]