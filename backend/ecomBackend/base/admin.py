from django.contrib import admin
from .models import Product
from .models import ShippingAddress
from .models import Order
from .models import Review
from .models import OrderItem
# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(Review)