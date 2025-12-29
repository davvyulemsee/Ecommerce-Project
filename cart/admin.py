from django.contrib import admin

# Register your models here.

# cart/admin.py
from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("session_key", "created_at", "updated_at")

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")