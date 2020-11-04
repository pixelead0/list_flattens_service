from app.main.models import ItemsProcessed
from django.contrib import admin


@admin.register(ItemsProcessed)
class ItemsProcessedAdmin(admin.ModelAdmin):
    """Admin for article catalog."""

    list_display = (
        "items",
        "result",
        "is_active",
        "updated_at",
    )

    search_fields = ("items", "result")

    ordering = ("-updated_at",)
