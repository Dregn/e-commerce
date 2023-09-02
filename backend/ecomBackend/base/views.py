from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Product
from rest_framework.decorators import permission_classes, api_view
from .serializer import ProductSerializer,UserSerializer,UserSerializerFromToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated ,IsAdminUser



def fetchRoutes(request):
    return JsonResponse("Hello", safe=False);



