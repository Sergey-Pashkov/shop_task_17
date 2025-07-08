from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ-панель для управления товарами.
    Настройка отображения и функциональности в административном интерфейсе.
    """
    # Поля, отображаемые в списке товаров
    list_display = ['name', 'price', 'created_at']
    
    # Поля для поиска
    search_fields = ['name', 'description']
    
    # Фильтры в боковой панели
    list_filter = ['created_at', 'price']
    
    # Поля только для чтения
    readonly_fields = ['created_at']
    
    # Порядок полей в форме редактирования
    fields = ['name', 'description', 'price', 'image', 'created_at']
