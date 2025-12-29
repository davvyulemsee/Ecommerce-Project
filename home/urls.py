from . import views
from django.urls import include, path

app_name = "storefront"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("search/", views.search, name="search"),
    path("category/<slug:slug>/", views.category_list, name="category"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("newsletter/subscribe/", views.newsletter_subscribe, name="newsletter_subscribe"),
]


