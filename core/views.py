from rest_framework import status
from .models import Customer, StoreItems, OrderItem
from .serializers import (
    CustomerSerializer,
    StoreItemsSerializer,
    OrderItemSerializer,
    NestedCustomerSerializer
)
from rest_framework.response import Response
from rest_framework.views import APIView


class CustomerAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            customer = Customer.objects.get(id=pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        else:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)


class StoreItemsAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            store_item = StoreItems.objects.get(id=pk)
            serializer = StoreItemsSerializer(store_item)
            return Response(serializer.data)
        else:
            store_items = StoreItems.objects.all()
            serializer = StoreItemsSerializer(store_items, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        
        store_item = StoreItems.objects.create(
            item_name = data['item_name'],
            is_returnable = data['is_returnable'],
            in_stock = data['in_stock']
        )
        
        serializer = StoreItemsSerializer(store_item)
        return Response(serializer.data)
    
    def patch(self, request, pk, format=None):
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


class OrderItemAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            order_item = OrderItem.objects.get(id=pk)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        else:
            order_items = OrderItem.objects.all()
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
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


class NestedCustomerAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            customer = Customer.objects.get(id=pk)
            serializer = NestedCustomerSerializer(customer)
            return Response(serializer.data)
        else:
            customers = Customer.objects.all()
            serializer = NestedCustomerSerializer(customers, many=True)
            return Response(serializer.data)
