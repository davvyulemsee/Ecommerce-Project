from django.contrib import admin

# Register your models here.

# catalog/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "featured", "active")
    list_filter = ("featured", "active", "category")
    search_fields = ("name", "description", "sku")
    prepopulated_fields = {"slug": ("name",)}