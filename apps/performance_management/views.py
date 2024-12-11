from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import PerformanceReview, GoalSetting, FeedbackMechanism
from apps.emp_management.models import Employee

def performance_reviews_list(request):
    performance_reviews = PerformanceReview.objects.all()
    return render(request, "performance_reviews/performance_reviews_list.html", {"performance_reviews": performance_reviews})

def add_performance_review(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        review_text = request.POST.get("review_text")
        appraisal_text = request.POST.get("appraisal_text")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            PerformanceReview.objects.create(
                employee=employee,
                review_text=review_text,
                appraisal_text=appraisal_text,
            )
            return redirect("performance_reviews_list")
        except Employee.DoesNotExist:
            return render(request, "performance_reviews/add_performance_review.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all()
            })
    else:
        employees = Employee.objects.all()
        return render(request, "performance_reviews/add_performance_review.html", {"employees": employees})


def review_details(request, review_id):
    review = get_object_or_404(PerformanceReview, pk=review_id)

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        review_text = request.POST.get("review_text")
        appraisal_text = request.POST.get("appraisal_text")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            review.employee = employee
            review.review_text = review_text
            review.appraisal_text = appraisal_text
            review.save()

            return redirect("performance_reviews_list")
        except Employee.DoesNotExist:
            return render(request, "performance_reviews/review_details.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all(),
                "review": review,
            })
    else:
        employees = Employee.objects.all()
        return render(request, "performance_reviews/review_details.html", {
            "employees": employees,
            "review": review,
        })


def goal_settings(request):
    goals = GoalSetting.objects.all()
    return render(request, "performance_management/goal_settings.html", {"goals": goals})


def feedback_mechanism(request):
    feedbacks = FeedbackMechanism.objects.all()
    return render(request, "performance_management/feedback_mechanism.html", {"feedbacks": feedbacks})