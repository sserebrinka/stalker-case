from django.contrib import admin
from .models import Cases, Items


@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rarity', 'price', 'content')
    list_filter = ['price']
