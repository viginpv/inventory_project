from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory_app.views import ProductViewSet, add_stock, remove_stock

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Base URL for the ProductViewSet routes
    path('api/add-stock/', add_stock, name='add-stock'),  # Function-based view for adding stock
    path('api/remove-stock/', remove_stock, name='remove-stock'),  # Function-based view for removing stock
]
