from django.db import models
from django.contrib.auth.models import User
import uuid
from versatileimagefield.fields import VersatileImageField

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProductID = models.BigIntegerField(unique=True)
    ProductCode = models.CharField(max_length=255, unique=True)
    ProductName = models.CharField(max_length=255)
    ProductImage = VersatileImageField(upload_to="uploads/", blank=True, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey(User, related_name="user_products", on_delete=models.CASCADE)
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)
    HSNCode = models.CharField(max_length=255, blank=True, null=True)
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)

    class Meta:
        db_table = "products_product"
        verbose_name = "product"
        verbose_name_plural = "products"
        unique_together = (("ProductCode", "ProductID"),)
        ordering = ("-CreatedDate", "ProductID")

class Variant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    options = models.JSONField()  # Store options as a list of strings

    class Meta:
        db_table = "products_variant"
        verbose_name = "variant"
        verbose_name_plural = "variants"
        unique_together = (("product", "name"),)

class StockEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    variant = models.ForeignKey(Variant, related_name="stock_entries", on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    entry_type = models.CharField(max_length=10, choices=[('purchase', 'Purchase'), ('sale', 'Sale')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products_stock_entry"
        verbose_name = "stock entry"
        verbose_name_plural = "stock entries"
