from django.urls import path
from .views import get_product, create_product, product_detail

urlpatterns = [
    path('products/', get_product, name='get_products'),
    path('products/create', create_product, name='crate_products'),
    path('products/<int:pk>', product_detail, name='product_detail'),
]