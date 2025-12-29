from django.db import models

# Create your models here.
# checkout/models.py
from django.db import models
from catalog.models import Product

class Order(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Order {self.pk} - {self.full_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def line_total(self):
        return self.price * self.quantity