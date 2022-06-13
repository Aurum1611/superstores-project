from rest_framework import viewsets
from .models import Customer, StoreItems, OrderItem
from .serializers import (
    CustomerSerializer,
    StoreItemsSerializer,
    OrderItemSerializer
)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class StoreItemsViewSet(viewsets.ModelViewSet):
    queryset = StoreItems.objects.all()
    serializer_class = StoreItemsSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
