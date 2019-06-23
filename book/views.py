from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer