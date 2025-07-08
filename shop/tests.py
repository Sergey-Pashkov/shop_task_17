from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product

# Create your tests here.

class ProductViewsTestCase(TestCase):
    """
    Тесты для представлений приложения shop.
    Проверяем корректность отображения страниц и обработку ошибок.
    """
    
    def setUp(self):
        """Настройка тестовых данных"""
        self.client = Client()
        
        # Создаем тестовый товар
        self.product = Product.objects.create(
            name="Тестовый товар",
            description="Описание тестового товара",
            price=999.99
        )
    
    def test_product_list_view(self):
        """Тест отображения списка товаров"""
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый товар")
        self.assertContains(response, "999.99")
    
    def test_product_detail_view_exists(self):
        """Тест отображения существующего товара"""
        response = self.client.get(
            reverse('shop:product_detail', args=[self.product.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)
    
    def test_product_detail_view_not_found(self):
        """Тест обработки ошибки - товар не найден"""
        # Пытаемся получить несуществующий товар
        non_existent_id = 99999
        response = self.client.get(
            reverse('shop:product_detail', args=[non_existent_id])
        )
        
        # Проверяем, что возвращается 404
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Товар не найден", status_code=404)
        self.assertContains(response, "Вернуться к каталогу", status_code=404)


class ProductModelTestCase(TestCase):
    """Тесты для модели Product"""
    
    def test_product_creation(self):
        """Тест создания товара"""
        product = Product.objects.create(
            name="Новый товар",
            description="Описание нового товара",
            price=1500.00
        )
        
        self.assertEqual(product.name, "Новый товар")
        self.assertEqual(product.price, 1500.00)
        self.assertTrue(product.created_at)
    
    def test_product_str_method(self):
        """Тест строкового представления товара"""
        product = Product.objects.create(
            name="Товар для теста",
            description="Описание",
            price=100.00
        )
        
        self.assertEqual(str(product), "Товар для теста")
