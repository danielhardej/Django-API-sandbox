from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated_at')

admin.site.register(Item, ItemAdmin)
