from . import views
from django.urls import include, path

app_name = 'catalog'

urlpatterns = [
    path('', views.all_products, name='all_products'),
]