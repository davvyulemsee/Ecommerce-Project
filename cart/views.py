from django.shortcuts import render

# Create your views here.
# cart/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from catalog.models import Product
from .models import Cart, CartItem

def _get_cart(request):
    session_key = request.session.session_key or request.session.create()
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return cart

@require_POST
def add_to_cart(request):
    product_id = request.POST.get("product_id")
    qty = int(request.POST.get("quantity", 1))
    product = get_object_or_404(Product, pk=product_id, active=True)
    cart = _get_cart(request)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += qty
    else:
        item.quantity = qty
    item.save()
    return redirect(request.POST.get("next", "cart:view_cart"))

def view_cart(request):
    cart = _get_cart(request)
    items = cart.items.select_related("product").all()
    context = {"cart": cart, "items": items}
    return render(request, "cart/view.html", context)

@require_POST
def remove_from_cart(request):
    item_id = request.POST.get("item_id")
    cart = _get_cart(request)
    cart.items.filter(pk=item_id).delete()
    return redirect("cart:view_cart")