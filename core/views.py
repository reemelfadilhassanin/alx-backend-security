from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse("Welcome to ALX Backend Security!")

class HelloAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello, ALX Backend Security!"}, status=status.HTTP_200_OK)
