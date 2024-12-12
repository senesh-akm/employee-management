from django.urls import path
from . import views

urlpatterns = [
    path("reviews/", views.performance_reviews_list, name="performance_reviews_list"),
    path("reviews/add/", views.add_performance_review, name="add_performance_review"),
    path("reviews/edit/<int:review_id>/", views.review_details, name="review_details"),

    path("goals/", views.goal_settings_list, name="goal_setting_list"),
    path("goals/add/", views.add_goal_setting, name="add_goal_setting"),
    path("goals/edit/<int:goal_id>/", views.goal_setting_details, name="goal_setting_details"),

    path("feedbacks/", views.feedback_list, name="feedback_list"),
    path("feedbacks/add/", views.add_feedback, name="add_feedback"),
    path("feedbacks/edit/<int:feedback_id>/", views.feedback_details, name="feedback_details"),
]