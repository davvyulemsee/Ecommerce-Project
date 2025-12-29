from django.db import models

# Create your models here.
# cart/models.py
from django.conf import settings
from django.db import models
from catalog.models import Product

class Cart(models.Model):
    session_key = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def items_count(self):
        return self.items.aggregate(total=models.Sum('quantity'))['total'] or 0

    def total_price(self):
        return sum(item.line_total() for item in self.items.all())

    def __str__(self):
        return f"Cart {self.session_key}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("cart", "product")

    def line_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"