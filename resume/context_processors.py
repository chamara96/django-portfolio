from datetime import datetime
from django.utils import timezone
from django.db.models.functions import TruncDay
from django.db.models import Count
from .models import Contact, Log


def dashboard(request):
    contacts = Contact.objects.all()
    logs = Log.objects.all()
    today = datetime.today().date()

    log_chart = logs.annotate(
        date=TruncDay('login_at')
    ).values("date").annotate(
        count=Count('id')
    ).order_by("-date")

    log_data = []
    for l in log_chart:
        log_data.append({
            "date": l["date"].strftime("%Y-%m-%d"),
            "count": l["count"]
        })

    return {
        "contacts_count": contacts.count(),
        "log_chart": log_data,
        "total_log_count": logs.count(),
        "today_log_count": logs.filter(login_at__date=today).count(),
        "last_log_time": logs.latest('login_at').login_at if logs else None,
        "last_contact_time": contacts.latest('created_at').created_at,
        "now_time": timezone.now(),
    }
