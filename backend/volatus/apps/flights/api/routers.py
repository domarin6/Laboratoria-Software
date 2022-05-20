from rest_framework.routers import DefaultRouter
from apps.flights.api.viewsets.general_views import *
from apps.flights.api.viewsets.flight_viewsets import FlightViewSet

router = DefaultRouter()

router.register(r'flights',FlightViewSet,basename = 'flights')
router.register(r'category-flights',CategoryFlightViewSet,basename = 'category_flights')

urlpatterns = router.urls