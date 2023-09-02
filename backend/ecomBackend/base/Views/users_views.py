from django.http import JsonResponse

from rest_framework.decorators import permission_classes, api_view
from ..serializer import UserSerializer, UserSerializerFromToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = UserSerializer(self.user).data
        for k, v in user.items():
            data[k] = v;

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    userSerialized = UserSerializer(user, many=False)
    return JsonResponse(userSerialized.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    user = User.objects.all()
    userSerialized = UserSerializer(user, many=True)
    return JsonResponse(userSerialized.data, safe=False)


@api_view(['POST'])
def registerUser(request):
    data = request.data
    user = User.objects.create_user(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    serilaized = UserSerializerFromToken(user, many=False)
    print(serilaized)
    return JsonResponse(serilaized.data)
