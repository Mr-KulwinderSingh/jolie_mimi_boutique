from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.shop_all, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]