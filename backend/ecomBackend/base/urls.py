from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
import rest_framework
from django.urls import path,include
from django.conf import settings

print("Django Rest Framework Version:", rest_framework.__version__)

urlpatterns = [
    path("", views.fetchRoutes, name="Routes"),

    path("products/", views.fetchAllProducts, name="products"),
    path("user/profile/", views.getUserProfile, name="user-profile"),
    path("user/AllUsers/", views.getUsers, name="users"),
    path("user/registerUser/", views.registerUser, name="users"),
    path("products/<pk>", views.fetchOneProduct, name="product"),
]
