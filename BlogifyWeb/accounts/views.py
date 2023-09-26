from django.shortcuts import render
from django.views import generic
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User


# Create your views here.
class AccountView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    