from django.contrib import admin
from .models import Cake

# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Cake,CakeAdmin)
