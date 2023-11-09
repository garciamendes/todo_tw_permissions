# Django
from django.contrib.auth import get_user_model

# Third party
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
