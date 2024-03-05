from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Career

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CareerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Adicionado para leitura

    class Meta:
        model = Career
        fields = ['id', 'user', 'created_datetime', 'title', 'content']
