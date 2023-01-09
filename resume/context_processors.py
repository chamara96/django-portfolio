from datetime import datetime
from django.utils import timezone
from .models import Contact, Log


def dashboard(request):
    contacts = Contact.objects.all()
    logs = Log.objects.all()
    today = datetime.today().date()

    return {
        "contacts_count": contacts.count(),
        "total_log_count": logs.count(),
        "today_log_count": logs.filter(login_at__date=today).count(),
        "last_log_time": logs.latest('login_at').login_at,
        "last_contact_time": contacts.latest('created_at').created_at,
        "now_time": timezone.now(),
    }
