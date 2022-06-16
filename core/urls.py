from django.urls import path
from .views import (
    CustomerAPI,
    StoreItemsAPI,
    OrderItemAPI,
    NestedCustomerAPI
)

urlpatterns = [
    path('customers/<int:pk>/', CustomerAPI.as_view()),
    path('customers/', CustomerAPI.as_view()),
    path('storeitems/<int:pk>/', StoreItemsAPI.as_view()),
    path('storeitems/', StoreItemsAPI.as_view()),
    path('orderitems/<int:pk>/', OrderItemAPI.as_view()),
    path('orderitems/', OrderItemAPI.as_view()),
    path('nestedcustomers/', NestedCustomerAPI.as_view()),
]
