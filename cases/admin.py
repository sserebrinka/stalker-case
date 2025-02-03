from django.contrib import admin
from django.utils.html import mark_safe
from .models import Cases, Items


@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'display_content', 'preview_image')
    list_filter = ['price']

    def display_content(self, obj):
        return ', '.join(obj.get_content())
    
    display_content.short_description = 'Content'

    def preview_image(self, obj):
        if obj.image:  
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'

    preview_image.short_description = 'Preview'


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rarity', 'value', 'get_probability', 'preview_image')
    list_filter = ['rarity']

    def display_probability(self, obj):
        return obj.get_probability()
    
    display_probability.short_description = 'Probability'

    def preview_image(self, obj):
        if obj.image:  
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'

    preview_image.short_description = 'Preview'