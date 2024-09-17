from django.contrib import admin
from .models import Outflow


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at')
    search_fields = ('product',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
