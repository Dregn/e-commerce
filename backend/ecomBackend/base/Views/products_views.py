from django.http import JsonResponse
from ..models import Product
from rest_framework.decorators import permission_classes, api_view
from ..serializer import ProductSerializer


@api_view(['GET'])
def fetchAllProducts(request):
    products = Product.objects.all();
    productserialized = ProductSerializer(products, many=True)
    return JsonResponse(productserialized.data, safe=False)


@api_view(['GET'])
def fetchOneProduct(request, pk):
    product = Product.objects.get(_id=pk);
    productSerialized = ProductSerializer(product, many=False)
    return JsonResponse(productSerialized.data, safe=False)
