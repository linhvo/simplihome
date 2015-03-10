from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import NestUser, SimplisafeUser
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    nest_users = serializers.PrimaryKeyRelatedField(many=True, queryset=NestUser.objects.all())
    simplisafe_users = serializers.PrimaryKeyRelatedField(many=True, queryset=SimplisafeUser.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nest_users', 'simplisafe_users', 'token')


class NestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NestUser

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token



class SimplisafeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimplisafeUser