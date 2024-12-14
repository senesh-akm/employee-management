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


def candidate_screening_list(request):
    candidate_screenings = CandidateScreening.objects.all()
    return render(request, "candidate_screening/candidate_screening_list.html", {"candidate_screenings": candidate_screenings})


def add_candidate_screening(request):
    if request.method == "POST":
        candidate = request.POST.get("candidate")
        job_position_id = request.POST.get("job_position")
        members = request.POST.get("members")
        conduct_interviews = request.POST.get("conduct_interviews")

        # Debugging output
        print(f"Candidate: {candidate}")
        print(f"Job Position ID: {job_position_id}")

        if not candidate:
            return render(request, "candidate_screening/add_candidate_screening.html", {
                "error_message": "Candidate field is required.",
                "job_positions": JobPosting.objects.all()
            })

        job_position = get_object_or_404(JobPosting, pk=job_position_id)
        CandidateScreening.objects.create(
            candidate=candidate,
            job_position=job_position,
            members=members,
            conduct_interviews=conduct_interviews
        )
        return redirect("candidate_screening_list")

    job_positions = JobPosting.objects.all()
    return render(request, "candidate_screening/add_candidate_screening.html", {
        "job_positions": job_positions
    })


def screening_details(request, screening_id):
    screening = get_object_or_404(CandidateScreening, pk=screening_id)

    if request.method == "POST":
        candidate = request.POST.get("candidate")
        job_position_id = request.POST.get("job_position")
        members = request.POST.get("members")
        conduct_interviews = request.POST.get("conduct_interviews")

        job_position = get_object_or_404(JobPosting, pk=job_position_id)
        screening.candidate = candidate
        screening.job_position = job_position
        screening.members = members
        screening.conduct_interviews = conduct_interviews
        screening.save()
        return redirect("candidate_screening_list")

    job_positions = JobPosting.objects.all()
    return render(request, "candidate_screening/screening_details.html", {
        "screening": screening,
        "job_positions": job_positions
    })


def onboarding_list(request):
    onboardings = OnboardingProcess.objects.all()
    return render(request, "onboarding_process/onboarding_list.html", {"onboardings": onboardings})


def add_onboarding(request):
    if request.method == "POST":
        candidate_id = request.POST.get("candidate")
        designation = request.POST.get("designation")
        joining_date = request.POST.get("joining_date")
        offer_letter = request.POST.get("offer_letter")

        # Ensure candidate exists and retrieve designation from candidate's job position
        candidate = get_object_or_404(CandidateScreening, pk=candidate_id)
        if not designation:  # If designation is not provided, default to the candidate's job position
            designation = candidate.job_position.title  # Use the job position's title for designation
        
        # Create the onboarding process
        OnboardingProcess.objects.create(
            candidate=candidate,
            designation=designation,
            joining_date=joining_date,
            offer_letter=offer_letter,
        )
        return redirect("onboarding_list")

    candidates = CandidateScreening.objects.all()
    return render(request, "onboarding_process/add_onboarding.html", {
        "candidates": candidates,
    })


def onboarding_details(request, onboarding_id):
    onboarding = get_object_or_404(OnboardingProcess, pk=onboarding_id)

    if request.method == "POST":
        candidate_id = request.POST.get("candidate")
        designation = request.POST.get("designation")
        joining_date = request.POST.get("joining_date")
        offer_letter = request.POST.get("offer_letter")

        candidate = get_object_or_404(CandidateScreening, pk=candidate_id)
        onboarding.candidate = candidate
        onboarding.designation = designation
        onboarding.joining_date = joining_date
        onboarding.offer_letter = offer_letter
        onboarding.save()
        return redirect("onboarding_list")

    candidates = CandidateScreening.objects.all()
    return render(request, "onboarding_process/onboarding_details.html", {
        "onboarding": onboarding,
        "candidates": candidates,
    })