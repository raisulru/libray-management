from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'category',
            'author',
            'publisher',
            'total',
            'description',
            'soft_copy'
        ]

        read_only_fields = ('id', )