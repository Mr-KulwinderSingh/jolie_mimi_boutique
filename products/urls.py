from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.shop_all, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]