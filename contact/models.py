from django.db import models
from django.utils.timezone import now

# Create your models here.
class Form(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)
    message = models.CharField(verbose_name="Mensaje", max_length=300)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")

    class Meta:
        verbose_name = "form"
        verbose_name_plural = "forms"
        ordering = ['-created']

    def __str__(self):
        return self.name
