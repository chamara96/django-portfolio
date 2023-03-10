from uuid import uuid4
import datetime
from django.core.validators import MaxValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def get_upload_path(instance, filename):
    """
    this method is use to define image name pattern with the instance name and
    current date time.
    :param instance:
    :param filename:
    :return:
    """
    ext = filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"
    return "/".join([instance.__class__.__name__, filename])


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
