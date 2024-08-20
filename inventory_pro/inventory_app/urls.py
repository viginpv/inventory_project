# inventory_pro/urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('api/create-product/', views.create_product, name='create_product'),
    path('api/list-products/', views.list_products, name='list_products'),
    path('api/stock/add/<int:subvariant_id>/', views.add_stock, name='add_stock'),
    path('api/remove-stock/<int:subvariant_id>/', views.remove_stock, name='remove_stock'),
    path('', TemplateView.as_view(template_name='index.html')),  # Serve React app
]
