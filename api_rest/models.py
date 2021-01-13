from django.db import models
from django.conf import settings

class Owner(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class Category(Owner):
    description = models.CharField(max_length=100, help_text='Descripcion de la  categoria', unique=True)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name_plural = 'Categorias'

class SubCategory(Owner):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text='Descripción de la Sub Categoría'
    )
 
    def __str__(self):
        return '{}:{}'.format(self.category.description, self.description)
 
    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('category','description')
 
 
class Product(Owner):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
    )
    creation_date = models.DateTimeField()
    sold = models.BooleanField(default=False)
 
    def __str__(self):
        return '{}'.format(self.description)
 
    class Meta:
        verbose_name_plural = "Productos"
