from django.shortcuts import render, redirect, get_object_or_404
from .models import TrainingNeedsAssessment, TrainingPlan, TrainingRecord
from apps.emp_management.models import Employee
from django.http import JsonResponse

def need_trainings_list(request):
    training_needs = TrainingNeedsAssessment.objects.all()
    return render(request, "training_needs/need_trainings_list.html", {"training_needs": training_needs})


def add_need_training(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        designation = request.POST.get("designation")
        duration = request.POST.get("duration")

        print(f"Submitted employee_id: {employee_id}")  # Debugging

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            TrainingNeedsAssessment.objects.create(
                employee=employee,
                designation=designation,
                duration=duration
            )
            return redirect("need_trainings_list")
        except Employee.DoesNotExist:
            print("Employee not found!")  # Debugging
            return render(request, "training_needs/add_need_training.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all()
            })
    else:
        employees = Employee.objects.all()
        return render(request, "training_needs/add_need_training.html", {"employees": employees})
    

def need_details(request, training_need_id):
    training_need = get_object_or_404(TrainingNeedsAssessment, pk=training_need_id)

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        designation = request.POST.get("designation")
        duration = request.POST.get("duration")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            training_need.employee = employee
            training_need.designation = designation
            training_need.duration = duration
            training_need.save()

            return redirect("need_trainings_list")
        except Employee.DoesNotExist:
            return render(request, "training_needs/need_details.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all(),
                "training_need": training_need,
            })

    employees = Employee.objects.all()
    return render(request, "training_needs/need_details.html", {
        "employees": employees,
        "training_need": training_need,
    })


def training_plans_list(request):
    tarining_plans = TrainingPlan.objects.all()
    return render(request, "training_plans/training_plans_list.html", {"tarining_plans": tarining_plans})


def add_training_plan(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        plan = request.POST.get("plan")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            TrainingPlan.objects.create(
                employee=employee,
                plan=plan,
            )
            return redirect("training_plans_list")
        except Employee.DoesNotExist:
            return render(request, "training_plans/add_training_plan.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all()
            })
    else:
        employees = Employee.objects.all()
        return render(request, "training_plans/add_training_plan.html", {"employees": employees})
    

def training_plan_view(request, plan_id):
    pln = get_object_or_404(TrainingPlan, pk=plan_id)

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        plan = request.POST.get("plan")

        try:
            employee = get_object_or_404(Employee, pk=employee_id)
            pln.employee = employee
            pln.plan = plan
            pln.save()

            return redirect("training_plans_list")
        except Employee.DoesNotExist:
            return render(request, "training_plans/training_plan_view.html", {
                "error_message": "Invalid employee selected. Please try again.",
                "employees": Employee.objects.all(),
                "plan": pln,
            })
    else:
        employees = Employee.objects.all()
        return render(request, "training_plans/training_plan_view.html", {
            "employees": employees,
            "plan": pln,
        })