
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Destination, Attraction
from .serializers import (
    DestinationSerializer,
    AttractionSerializer
)


class DestinationViewSet(viewsets.ModelViewSet):

    queryset = Destination.objects.all()

    serializer_class = DestinationSerializer

    permission_classes = [
        AllowAny
    ]


class AttractionViewSet(viewsets.ModelViewSet):

    queryset = Attraction.objects.all()

    serializer_class = AttractionSerializer

    permission_classes = [
        AllowAny
    ]