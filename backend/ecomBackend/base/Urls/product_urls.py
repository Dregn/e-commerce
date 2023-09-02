from django.urls import path
from ..Views import products_views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
import rest_framework

print("Django Rest Framework Version:", rest_framework.__version__)
urlpatterns = [
    path("", views.fetchAllProducts, name="products"),
    path("<pk>", views.fetchOneProduct, name="product"),
]
