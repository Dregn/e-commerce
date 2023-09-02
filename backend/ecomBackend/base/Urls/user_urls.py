from django.urls import path
from django.urls import path
from ..Views import users_views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
import rest_framework

print("Django Rest Framework Version:", rest_framework.__version__)
urlpatterns = [
    path("profile/", views.getUserProfile, name="user-profile"),
    path("AllUsers/", views.getUsers, name="users"),
    path("registerUser/", views.registerUser, name="register-user"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]