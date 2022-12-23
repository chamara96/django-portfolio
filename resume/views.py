from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import *
from .forms import ContactForm
import requests
from constance import config

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "type": "success",
                "message": "Sample Response",
            })

    else:
        form = ContactForm()

        basic_info = BasicInfo.objects.latest()

        stacks = Stack.objects.values_list('title', flat=True)
        stacks = ", ".join(stacks)

        tech_skills = TechSkill.objects.all()

        social_media = SocialMedia.objects.all()

        reviews = Review.objects.all()

        certificates = Certificate.objects.all()

        publications = Publication.objects.all()

        experiences = Experience.objects.all()

        projects = Project.objects.all()

        blogs = Blog.objects.all()

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
        return render(request, 'index.html', context)


def fiverr_reviews():
    url = "https://www.fiverr.com/reviews/user_page/fetch_user_reviews/79556254?user_id=79556254&as_seller=true"
    x = requests.get(url)
    print(x.status_code)
