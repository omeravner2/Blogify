
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import *


# Create your views here.
class AccountView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return JsonResponse({'message': 'User registered'})
        else:
            return JsonResponse({'message': 'Username already exists'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            userserializer = UserSerializer(user).data
            return JsonResponse({'message': 'Login successful', 'user': userserializer}, status=200)
        else:
            return JsonResponse({'message': 'Login failed'}, status=401)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


def logout_view(request):
    logout(request)
    # Return JSON response indicating successful logout
    return JsonResponse({'message': 'Logout successful'})

