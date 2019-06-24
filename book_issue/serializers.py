from rest_framework import serializers
from .models import IssueBook
from users.serializers import UserSerializer
from book.serializers import BookSerializer


class IssueBookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    issue_by = UserSerializer()
    accept_by = UserSerializer()

    class Meta:
        model = IssueBook
        fields = [
            'id',
            'user',
            'book',
            'issue_by',
            'accept_by',
            'issue_date',
            'suggest_return_date',
            'return_date',
            'status'
        ]

        read_only_fields = ('id', )