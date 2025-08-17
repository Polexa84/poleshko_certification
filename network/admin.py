from django.contrib import admin
from .models import Network, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'supplier', 'debt', 'level')
    list_filter = ('city',)  # Фильтр по городу
    search_fields = ('name', 'city')
    readonly_fields = ('creation_time', 'level') # Только для чтения
    actions = ['clear_debt'] # Action для очистки задолженности

    # Отображение поставщика как ссылки
    def supplier_link(self, obj):
        if obj.supplier:
            return f'<a href="/admin/network/network/{obj.supplier.id}/change/">{obj.supplier.name}</a>'
        return None
    supplier_link.short_description = 'Поставщик'
    supplier_link.allow_tags = True
    list_display = ('name', 'email', 'city', 'supplier_link', 'debt', 'level') #Добавили supplier_link в отображение

    # Admin Action для очистки задолженности
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = "Очистить задолженность перед поставщиком"