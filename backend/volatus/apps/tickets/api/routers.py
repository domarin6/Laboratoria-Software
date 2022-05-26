from rest_framework.routers import DefaultRouter
from apps.tickets.api.viewsets.shoppingCart_viewsets import *


router = DefaultRouter()

router.register(r'shoppingCart',shoppingCartViewSet, basename = 'shoppingCart')

urlpatterns = router.urls