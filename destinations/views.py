
from rest_framework import viewsets

from .models import Destination, Attraction
from .serializers import (
    DestinationSerializer,
    AttractionSerializer
)


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer