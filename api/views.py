# api/views.py
from django.http import JsonResponse, HttpResponse
from .models import User

def user_list(request):
    users = User.objects.all()
    data = {"users": list(users.values("id", "username", "email"))}
    return JsonResponse(data)


def homepage(request):
    return HttpResponse("<h1>Welcome to RentApp</h1>")