from django.db import models

# Create your models here.
class Category(models.Model):
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name_plural = 'Categorias'
