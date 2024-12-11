from django.urls import path
from . import views

urlpatterns = [
    path("reviews/", views.performance_reviews_list, name="performance_reviews_list"),
    path("reviews/add/", views.add_performance_review, name="add_performance_review"),
    path("reviews/edit/<int:review_id>/", views.review_details, name="review_details"),

    path("goals/", views.goal_settings, name="goal_settings"),

    path("feedbacks/", views.feedback_mechanism, name="feedback_mechanism"),
]