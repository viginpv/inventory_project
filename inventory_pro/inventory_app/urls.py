# urls.py
from django.urls import path
from .views import create_product, list_products, add_stock, remove_stock,home

urlpatterns = [
    path('', home, name='home'),
    path('api/products/create/', create_product, name='create_product'),
    path('api/products/', list_products, name='list_products'),
    path('api/stock/add/<int:subvariant_id>/', add_stock, name='add_stock'),
    path('api/stock/remove/<int:subvariant_id>/', remove_stock, name='remove_stock'),
]
