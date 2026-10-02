from rest_framework.routers import DefaultRouter

from .views import (
    DestinationViewSet,
    AttractionViewSet
)

router = DefaultRouter()

router.register(
    r'destinations',
    DestinationViewSet,
    basename='destination'
)

router.register(
    r'attractions',
    AttractionViewSet,
    basename='attraction'
)

urlpatterns = router.urls