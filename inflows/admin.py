from django.contrib import admin
from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at')
    search_fields = ('supplier', 'product')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
