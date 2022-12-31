from django.http import JsonResponse
from django.shortcuts import render
from constance import config

from .forms import ContactForm
from . import utils as db_utils


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "type": "success",
                "message": "Thanks for your response...",
            })
        return JsonResponse({
            "type": "danger",
            "message": " ".join(str(err[0]) for err in form.errors.values()),
        })

    else:
        form = ContactForm()

        basic_info = db_utils.get_basic_info()
        stacks = db_utils.get_stacks()
        tech_skills = db_utils.get_techskills()
        social_media = db_utils.get_socialmedia()
        reviews = db_utils.get_reviews()
        certificates = db_utils.get_certificates()
        publications = db_utils.get_publications()
        experiences = db_utils.get_experiences()
        projects = db_utils.get_projects()
        blogs = db_utils.get_blogs()

        db_utils.create_user_logs(request)

        context = {
            "basic": basic_info,
            "reviews": reviews,
            "stacks": stacks,
            "tech_skills": tech_skills,
            "social_media": social_media,
            "experiences": experiences,
            "certificates": certificates,
            "publications": publications,
            "projects": projects,
            "blogs": blogs,
            "form": form,
            "config": config,
        }
        return render(request, 'resume/index.html', context)
