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
        
    def update(self, instance, valid_data):
        instance.customer = valid_data.get(
            'customer',
            instance.customer
        )
        
        if valid_data.get('items'):
            instance.items.set(valid_data['items'])
        
        instance.status = valid_data.get(
            'status',
            instance.status
        )
        instance.created_on = valid_data.get(
            'created_on',
            instance.created_on
        )
        
        instance.save()
        return instance
