from django.db import models


class Customer(models.Model):    
    name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=4,decimal_places=1)
    created_on = models.DateField(auto_now_add=True)
    phonenumber = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    @property
    def order_item_set(self):
        return OrderItem.objects.filter(customer=self.id)


class StoreItems(models.Model):
    item_name = models.CharField(max_length=50)
    
    RETURNABLE = 'RT'
    REPLACEMENT = 'RP'
    is_returnable_choices = [
        (RETURNABLE, 'Returnable'),
        (REPLACEMENT, 'Replacement'),
    ]
    is_returnable = models.CharField(
        max_length=2,
        choices=is_returnable_choices
    )
    
    YES = 'YS'
    NO = 'NO'
    in_stock_choices = [
        (YES, 'Yes'),
        (NO, 'No')
    ]
    in_stock = models.CharField(
        max_length=2,
        choices=in_stock_choices
    )
    
    def __str__(self) -> str:
        return self.item_name


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(StoreItems)
    
    DELIVERED = 'DL'
    ON_THE_WAY = 'OW'
    SHIPPED = 'SH'
    status_choices = [
        (DELIVERED, 'Delivered'),
        (ON_THE_WAY, 'On The Way'),
        (SHIPPED, 'Shipped')
    ]
    status = models.CharField(
        max_length=2,
        choices=status_choices
    )
    created_on = models.DateField(auto_now_add=True)
