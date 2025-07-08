from django.db import models

# Create your models here.

class Product(models.Model):
    """
    Модель товара для интернет-магазина.
    Содержит основную информацию о товаре: название, описание, цену, изображение и дату создания.
    """
    # Название товара (максимум 200 символов)
    name = models.CharField(max_length=200, verbose_name="Название товара")
    
    # Описание товара (текстовое поле без ограничений)
    description = models.TextField(verbose_name="Описание товара")
    
    # Цена товара (decimal поле для точности расчетов)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    
    # Изображение товара (путь к файлу изображения)
    image = models.ImageField(upload_to='products/', verbose_name="Изображение", blank=True, null=True)
    
    # Дата и время создания записи (автоматически устанавливается при создании)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']  # Сортировка по дате создания (новые сначала)

    def __str__(self):
        """Строковое представление товара - возвращает название"""
        return self.name
