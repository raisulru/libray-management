from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    get_full_name = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar',
            'get_full_name'
        ]

        read_only_fields = ('id', )