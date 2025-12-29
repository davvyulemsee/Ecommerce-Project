from django.shortcuts import render
import requests
from django.shortcuts import render
from django.db.models import Q
from catalog.models import Product


# Create your views here.

def index(request):
    return render(request, 'index.html')

# storefront/views.py
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Category, Product
from cart.models import Cart, CartItem
from checkout.forms import NewsletterForm
from django.views.decorators.http import require_POST

def home(request):
    categories = Category.objects.all()[:6]
    featured_products = Product.objects.filter(active=True, featured=True)[:8]
    context = {
        "categories": categories,
        "featured_products": featured_products,
    }
    return render(request, "home.html", context)

# def category_list(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     products = category.products.filter(active=True)
#     context = {
#         "category": category,
#         "products": products,
#     }
#     return render(request, "category.html", context)
#
# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, active=True)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
#
# @require_POST
# def newsletter_subscribe(request):
#     form = NewsletterForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return redirect(request.META.get("HTTP_REFERER", "home"))
#
# def about(request):
#     return render(request, "about.html")
#
# def search(request):
#     q = request.GET.get("q", "").strip()
#     results = Product.objects.none()
#     if q:
#         results = Product.objects.filter(
#             Q(name__icontains=q) | Q(description__icontains=q)
#         ).distinct()
#     context = {"query": q, "results": results}
#     return render(request, "storefront/search_results.html", context)
