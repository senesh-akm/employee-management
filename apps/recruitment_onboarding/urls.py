from django.urls import path
from . import views

urlpatterns = [
    path("job-postings/", views.job_posts_list, name="job_posts_list"),
    path("job-postings/add/", views.add_job_post, name="add_job_post"),
    path("job-postings/edit/<int:job_post_id>/", views.view_job_post, name="view_job_post"),

    path("candidate-screening/", views.candidate_screening_list, name="candidate_screening_list"),
    path("candidate-screening/add/", views.add_candidate_screening, name="add_candidate_screening"),
    path("candidate-screening/edit/<int:screening_id>/", views.screening_details, name="screening_details"),

    path("onboarding-process/", views.onboarding_list, name="onboarding_list"),
    path("onboarding-process/add/", views.add_onboarding, name="add_onboarding"),
    path("onboarding-process/edit/<int:onboarding_id>/", views.onboarding_details, name="onboarding_details"),
]