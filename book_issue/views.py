from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IssueBookSerializer
from .models import IssueBook


class IssueBookView(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer