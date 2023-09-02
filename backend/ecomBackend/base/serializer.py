from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product;
        fields = '__all__';


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User;
        fields = ['id', 'username', 'email', '_id', 'isAdmin', 'name'];

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

    def get__id(self, obj):
        _id = obj.id
        return _id

    def get_isAdmin(self, obj):
        isAdmin = obj.is_staff
        return isAdmin


class UserSerializerFromToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', '_id', 'isAdmin', 'name', 'token'];

    def get_token(self, obj):
        token = RefreshToken.for_user(obj);
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token
