from app.main.models import ItemsProcessed
from rest_framework import serializers


class ItemsProcessedSerializer(serializers.ModelSerializer):
    """ItemsProcessed Serializer."""

    class Meta:
        model = ItemsProcessed
        read_only_fields = ("result",)
        exclude = (
            "is_active",
            "created_at",
            "updated_at",
        )
