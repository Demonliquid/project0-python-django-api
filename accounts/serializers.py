from rest_framework import serializers
from allauth.account.adapter import get_adapter
from config import settings
from .models import User
from allauth.account.utils import setup_user_email


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
