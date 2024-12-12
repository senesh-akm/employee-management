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


def goal_settings_list(request):
    goals = GoalSetting.objects.all()
    return render(request, "goal_settings/goal_setting_list.html", {"goals": goals})


def add_goal_setting(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        goals = request.POST.get("goals")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            GoalSetting.objects.create(
                employee=employee,
                goals=goals,
            )
            return redirect("goal_setting_list")
        except Employee.DoesNotExist:
            return render(request, "goal_settings/add_goal_setting.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all()
            })
    else:
        employees = Employee.objects.all()
        return render(request, "goal_settings/add_goal_setting.html", {"employees": employees})


def goal_setting_details(request, goal_id):
    goal = get_object_or_404(GoalSetting, pk=goal_id)

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        goals = request.POST.get("goals")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            goal.employee = employee
            goal.goals = goals
            goal.save()

            return redirect("goal_setting_list")
        except Employee.DoesNotExist:
            return render(request, "goal_settings/goal_setting_details.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all(),
                "goal": goal,
            })
    else:
        employees = Employee.objects.all()
        return render(request, "goal_settings/goal_setting_details.html", {
            "employees": employees,
            "goal": goal,
        })


def feedback_list(request):
    feedbacks = FeedbackMechanism.objects.all()
    return render(request, "feedback_mechanism/feedback_list.html", {"feedbacks": feedbacks})


def add_feedback(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        feedback = request.POST.get("feedback")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            FeedbackMechanism.objects.create(
                employee=employee,
                feedback=feedback,
            )
            return redirect("feedback_list")
        except Employee.DoesNotExist:
            return render(request, "feedback_mechanism/add_feedback.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all()
            })
    else:
        employees = Employee.objects.all()
        return render(request, "feedback_mechanism/add_feedback.html", {"employees": employees})


def feedback_details(request, feedback_id):
    fb = get_object_or_404(FeedbackMechanism, pk=feedback_id)

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        feedback = request.POST.get("feedback")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            fb.employee = employee
            fb.feedback = feedback
            fb.save()

            return redirect("feedback_list")
        except Employee.DoesNotExist:
            return render(request, "feedback_mechanism/feedback_details.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all(),
                "fb": fb,
            })
    else:
        employees = Employee.objects.all()
        return render(request, "feedback_mechanism/feedback_details.html", {
            "employees": employees,
            "fb": fb,
        })