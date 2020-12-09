from django.contrib import admin
from .models import Cake, Dessert

# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Cake,CakeAdmin)

class DessertAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Dessert,DessertAdmin)
