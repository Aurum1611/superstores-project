from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import (
    CustomerViewSet,
    StoreItemsViewSet,
    OrderItemViewSet
)

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'storeitems', StoreItemsViewSet)
router.register(r'orderitems', OrderItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
