from django.http import JsonResponse
from ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', method='GET', block=True)
@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def login_view(request):
    return JsonResponse({"message": "Login endpoint"})
