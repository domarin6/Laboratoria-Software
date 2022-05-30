from rest_framework.routers import DefaultRouter
from apps.tickets.api.viewsets.shoppingCart_viewsets import *
from apps.tickets.api.viewsets.payment_viewsets import *

router = DefaultRouter()

router.register(r'shoppingCart',shoppingCartViewSet, basename = 'shoppingCart')
router.register(r'payment',CardViewset, basename = 'payment')
router.register(r'wallet',WalletViewSet, basename = 'wallet')


urlpatterns = router.urls