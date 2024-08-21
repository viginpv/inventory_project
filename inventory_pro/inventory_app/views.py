from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Variant
from .serializers import ProductSerializer, VariantSerializer
from rest_framework import status
from .models import Variant, StockEntry
from .models import Product
from .models import Variant, StockEntry
from .serializers import StockEntrySerializer

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@api_view(['POST'])
def create_product(request):
    data = request.data
    product_serializer = ProductSerializer(data=data)
    
    if product_serializer.is_valid():
        product = product_serializer.save()
        variants_data = data.get('variants', [])

        for variant_data in variants_data:
            variant_data['product'] = product.id
            variant_serializer = VariantSerializer(data=variant_data)
            if variant_serializer.is_valid():
                variant_serializer.save()
            else:
                return Response(variant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
def add_stock(request):
    data = request.data
    variant_id = data.get('variant_id')
    quantity = data.get('quantity')

    try:
        variant = Variant.objects.get(id=variant_id)
    except Variant.DoesNotExist:
        return Response({"error": "Variant not found"}, status=status.HTTP_404_NOT_FOUND)

    stock_entry = StockEntry(variant=variant, quantity=quantity, entry_type='purchase')
    stock_entry.save()

    variant.product.TotalStock += quantity
    variant.product.save()

    return Response({"status": "Stock added"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def remove_stock(request):
    data = request.data
    variant_id = data.get('variant_id')
    quantity = data.get('quantity')

    try:
        variant = Variant.objects.get(id=variant_id)
    except Variant.DoesNotExist:
        return Response({"error": "Variant not found"}, status=status.HTTP_404_NOT_FOUND)

    if variant.product.TotalStock < quantity:
        return Response({"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST)

    stock_entry = StockEntry(variant=variant, quantity=quantity, entry_type='sale')
    stock_entry.save()

    variant.product.TotalStock -= quantity
    variant.product.save()

    return Response({"status": "Stock removed"}, status=status.HTTP_200_OK)