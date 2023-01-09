from .models import *
from user_agent_parser import Parser
from utils import get_client_ip


def get_basic_info():
    return BasicInfo.objects.filter(is_active=True).latest()


def get_stacks():
    stacks = Stack.objects.filter(is_active=True).values_list('title', flat=True)
    stacks = ", ".join(stacks)
    return stacks


def get_techskills():
    return TechSkill.objects.filter(is_active=True)


def get_socialmedia():
    return SocialMedia.objects.filter(is_active=True)


def get_reviews():
    return Review.objects.filter(is_active=True)


def get_certificates():
    return Certificate.objects.filter(is_active=True)


def get_publications():
    return Publication.objects.filter(is_active=True)


def get_experiences():
    return Experience.objects.filter(is_active=True)


def get_projects():
    return Project.objects.filter(is_active=True)


def get_demos():
    return Demo.objects.filter(is_active=True)


def get_blogs():
    return Blog.objects.filter(is_active=True)


def create_user_logs(request):
    ip_address = get_client_ip(request)
    ua_parser = Parser(request.META["HTTP_USER_AGENT"])
    device_name = ua_parser.device_name if ua_parser.device_name else None
    os = str(ua_parser.os) + " " + str(ua_parser.os_version)

    Log.objects.create(
        ip_address=ip_address,
        device_type=str(ua_parser.device_type),
        device_name=device_name,
        os=os,
        browser=ua_parser.browser,
    )
