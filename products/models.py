from django.db import models
import uuid
from versatileimagefield.fields import VersatileImageField

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProductID = models.BigIntegerField(unique=True)
    ProductCode = models.CharField(max_length=255, unique=True)
    ProductName = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey("auth.User", related_name="user%(class)s_objects", on_delete=models.CASCADE)
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)
    HSNCode = models.CharField(max_length=255, blank=True, null=True)
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)

    name = models.CharField(max_length=200, default="Unnamed Product")
    description = models.TextField(default="No description available")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    hsn_code = models.CharField(max_length=20, default="Unknown")

    # Correct unique_together placement
    class Meta:
        db_table = "products_product"
        verbose_name = "product"
        verbose_name_plural = "products"
        unique_together = (("ProductCode", "ProductID"),)  # Enforcing uniqueness for the combination
        ordering = ("-CreatedDate", "ProductID")

class Variant(models.Model):
    product = models.ForeignKey(
        Products, related_name="variants", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    # Optional: Add an options method or property to manage variant options
    def options(self):
        # Placeholder or logic to handle options for the variant
        return ", ".join([option.name for option in self.subvariant_set.all()])  # Example logic

    options.short_description = "Options"  # Display name in the admin panel

    def __str__(self):
        return f"{self.name} ({self.product.ProductName})"

class SubVariant(models.Model):
    variant = models.ForeignKey(
        Variant, related_name="subvariant_set", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - Stock: {self.stock}"



