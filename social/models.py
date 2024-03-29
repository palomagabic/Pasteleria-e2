from django.db import models
from django.utils.timezone import now
# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=100)
    url = models.URLField(verbose_name="Link", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "link"
        verbose_name_plural = "link"
        ordering = ['name']

    def __str__(self):
        return self.name
