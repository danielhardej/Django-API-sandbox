from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=['get'])
    def get_item_by_id(self, request, pk=None):
        try:
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=404)