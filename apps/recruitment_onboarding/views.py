from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import JobPosting, CandidateScreening, OnboardingProcess
from apps.emp_management.models import Employee

def job_posts_list(request):
    job_posts = JobPosting.objects.all()
    return render(request, "job_posting/job_posts_list.html", {"job_posts": job_posts})


def add_job_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        responsibilities = request.POST.get("responsibilities")
        requirements = request.POST.get("requirements")
        work_type = request.POST.get("work_type")
        employee_type = request.POST.get("employee_type")
        offers = request.POST.get("offers")

        try:
            JobPosting.objects.create(
                title=title,
                description=description,
                responsibilities=responsibilities,
                requirements=requirements,
                work_type=work_type,
                employee_type=employee_type,
                offers=offers,
            )
            return redirect("job_posts_list")
        except Exception as e:
            return render(request, "job_posting/add_job_post.html", {
                "error_message": "An error occurred while creating the job post. Please try again.",
            })
    else:
        return render(request, "job_posting/add_job_post.html")
    

def view_job_post(request, job_post_id):
    job_post = get_object_or_404(JobPosting, pk=job_post_id)

    if request.method == "POST":
        job_post.title = request.POST.get("title")
        job_post.description = request.POST.get("description")
        job_post.responsibilities = request.POST.get("responsibilities")
        job_post.requirements = request.POST.get("requirements")
        job_post.work_type = request.POST.get("work_type")
        job_post.employee_type = request.POST.get("employee_type")
        job_post.offers = request.POST.get("offers")

        job_post.save()
        return redirect("job_posts_list")

    return render(request, "job_posting/view_job_post.html", {"job_post": job_post})