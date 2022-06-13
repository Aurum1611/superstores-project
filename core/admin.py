from django.contrib import admin
from .models import Customer, StoreItems, OrderItem

admin.site.register(Customer)
admin.site.register(StoreItems)
admin.site.register(OrderItem)
