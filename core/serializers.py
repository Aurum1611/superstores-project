from rest_framework import serializers
from .models import Customer, StoreItems, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'age', 'created_on',
                  'phonenumber', 'is_active')


class StoreItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItems
        fields = ('id', 'item_name', 'is_returnable',
                  'in_stock')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'customer', 'items', 'status',
                  'created_on')
