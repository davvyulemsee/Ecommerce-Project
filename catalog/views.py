from django.shortcuts import render
from .models import Product
from django.contrib import messages


# Create your views here.

def all_products(request):
    category = request.GET.get('category')
    query = request.GET.get('q')

    gigs = Product.objects.all()

    if category:
        gigs = gigs.filter(category=category)
    if query:
        gigs = gigs.filter(title__icontains=query)

    return render(request, 'catalog.html')
