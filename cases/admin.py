from django.contrib import admin
from .models import Cases, Items


@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'display_content')
    list_filter = ['price']

    def display_content(self, obj):
        return ', '.join(obj.get_content())
    
    display_content.short_description = 'Content'


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rarity', 'value', 'get_probability')
    list_filter = ['rarity']

    def display_probability(self, obj):
        return obj.get_probability()
    
    display_probability.short_description = 'Probability'