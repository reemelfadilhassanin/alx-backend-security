from .models import RequestLog
from django.utils.timezone import now
from ipware import get_client_ip  # install django-ipware

class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, _ = get_client_ip(request)
        if ip:
            RequestLog.objects.create(
                ip_address=ip,
                timestamp=now(),
                path=request.path
            )
        return self.get_response(request)
