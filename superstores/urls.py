from django.contrib import admin
from django.urls import path
from core.views import (
    CustomerAPI,
    StoreItemsAPI,
    OrderItemAPI,
    NestedCustomerViewSet
)

urlpatterns = [
    path('customers/<int:pk>/', CustomerAPI.as_view()),
    path('customers/', CustomerAPI.as_view()),
    path('storeitems/<int:pk>/', StoreItemsAPI.as_view()),
    path('storeitems/', StoreItemsAPI.as_view()),
    path('orderitems/<int:pk>/', OrderItemAPI.as_view()),
    path('orderitems/', OrderItemAPI.as_view()),
    path('nestedcustomer/', NestedCustomerViewSet.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
]
