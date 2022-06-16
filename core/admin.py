from django.contrib import admin
from .models import Customer, StoreItems, OrderItem


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phonenumber',)


class OrderItemAdmin(admin.ModelAdmin):
    list_filter = ('status',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreItems)
admin.site.register(OrderItem, OrderItemAdmin)
