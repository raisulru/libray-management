from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer