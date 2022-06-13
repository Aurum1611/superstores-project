from rest_framework import viewsets, status
from .models import Customer, StoreItems, OrderItem
from .serializers import (
    CustomerSerializer,
    StoreItemsSerializer,
    OrderItemSerializer,
    NestedCustomerSerializer
)
from rest_framework.response import Response


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class StoreItemsViewSet(viewsets.ModelViewSet):
    queryset = StoreItems.objects.all()
    serializer_class = StoreItemsSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        store_item = StoreItems.objects.create(
            item_name = data['item_name'],
            is_returnable = data['is_returnable'],
            in_stock = data['in_stock']
        )
        store_item.save()
        
        serializer = StoreItemsSerializer(store_item)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        store_item = self.get_object()
        data = request.data
        
        store_item.item_name = data.get(
            'item_name',
            store_item.item_name
        )
        store_item.is_returnable = data.get(
            'is_returnable',
            store_item.is_returnable
        )
        store_item.in_stock = data.get(
            'in_stock',
            store_item.in_stock
        )
        
        store_item.save()
        
        serializer = StoreItemsSerializer(store_item)
        return Response(serializer.data)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        def is_store_item_valid(item_ids: list)-> bool:
            for item_id in item_ids:
                if not StoreItems.objects.filter(id=item_id).exists():
                    return False
            else:
                return True
        
        if Customer.objects.filter(id=data['customer']).exists() \
        and is_store_item_valid(data['items']):
            
            order_item = OrderItem.objects.create(
                customer=Customer.objects.get(id=data['customer']),
                status=data['status'],
                created_on=data['created_on']
            )
            
            order_item.items.set(StoreItems.objects
                                 .filter(id__in=data['items']))

            order_item.save()

            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        else:
            return Response('Invalid customer or item id',
                            status=status.HTTP_403_FORBIDDEN)


class NestedCustomerViewSet(CustomerViewSet):
    serializer_class = NestedCustomerSerializer
