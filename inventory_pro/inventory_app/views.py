# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Products, Variant, SubVariant
from .serializers import ProductSerializer
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

@api_view(['POST'])
def create_product(request):
    data = request.data
    product_name = data.get('ProductName')
    variants = data.get('variants')

    if not product_name:
        return Response({'error': 'Product name is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Create the product
        product = Products.objects.create(ProductName=product_name, CreatedUser=request.user)

        for variant_data in variants:
            # Create the variant
            variant = Variant.objects.create(product=product, name=variant_data['name'])
            for option in variant_data['options']:
                # Create subvariants
                SubVariant.objects.create(variant=variant, name=option)

        return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error creating product: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_stock(request, subvariant_id):
    try:
        subvariant = SubVariant.objects.get(id=subvariant_id)
        stock_to_add = request.data.get('stock', 0)
        subvariant.stock += int(stock_to_add)
        subvariant.save()
        return Response({'status': 'stock added'}, status=status.HTTP_200_OK)
    except SubVariant.DoesNotExist:
        return Response({'error': 'SubVariant not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def remove_stock(request, subvariant_id):
    try:
        subvariant = SubVariant.objects.get(id=subvariant_id)
        stock_to_remove = request.data.get('stock', 0)
        if subvariant.stock >= stock_to_remove:
            subvariant.stock -= stock_to_remove
            subvariant.save()
            return Response({'status': 'stock removed'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
    except SubVariant.DoesNotExist:
        return Response({'error': 'SubVariant not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
