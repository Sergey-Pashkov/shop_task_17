"""
URL-конфигурация для приложения shop.
Определяет маршруты для представлений интернет-магазина.
"""

from django.urls import path
from . import views

# Имя приложения для пространства имен URL
app_name = 'shop'

urlpatterns = [
    # Главная страница с каталогом товаров
    path('', views.product_list, name='product_list'),
    
    # Страница детального просмотра товара
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
