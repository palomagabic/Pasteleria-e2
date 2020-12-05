from django.db import models

# Create your models here.
class Cake(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Titulo")
    descripcion = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen")
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha modificacion")

    class Meta:
        verbose_name = "torta"
        verbose_name_plural = "tortas"
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
