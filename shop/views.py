from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    """
    Представление для отображения списка всех товаров.
    Получает все товары из базы данных и передает их в шаблон.
    """
    # Получаем все товары, отсортированные по дате создания (новые сначала)
    products = Product.objects.all()
    
    # Передаем товары в контексте шаблона
    context = {
        'products': products,
        'title': 'Каталог товаров'
    }
    
    return render(request, 'shop/product_list.html', context)


def product_detail(request, product_id):
    """
    Представление для отображения детальной информации о товаре.
    Принимает ID товара и отображает всю информацию о нем.
    Если товар не найден, возвращает страницу 404 с рекомендациями.
    """
    # Получаем товар по ID или возвращаем 404, если не найден
    try:
        product = get_object_or_404(Product, id=product_id)
    except:
        # Если товар не найден, получаем другие товары для рекомендаций
        other_products = Product.objects.all()[:3]  # Первые 3 товара
        context = {
            'other_products': other_products,
            'title': 'Товар не найден'
        }
        return render(request, '404.html', context, status=404)
    
    # Передаем товар в контексте шаблона
    context = {
        'product': product,
        'title': f'Товар: {product.name}'
    }
    
    return render(request, 'shop/product_detail.html', context)
