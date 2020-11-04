
# Django REST Framework
from rest_framework import generics

# Models
from app.main.models import ItemsProcessed

# Serializers
from app.main.serializers import ItemsProcessedSerializer


class ItemsProcessedCreate(generics.CreateAPIView):
    queryset = ItemsProcessed.objects.actives()
    serializer_class = ItemsProcessedSerializer
