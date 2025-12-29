# cart/urls.py
from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add/", views.add_to_cart, name="add_to_cart"),
    path("remove/", views.remove_from_cart, name="remove_from_cart"),
]