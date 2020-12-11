from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'name', 'email', 'message')
    list_display = ('name', 'email', 'message', 'created')
    search_fields = ('email','created')

admin.site.register(Form, FormAdmin)
