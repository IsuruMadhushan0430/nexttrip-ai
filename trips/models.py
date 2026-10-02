from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from destinations.models import Destination


class Trip(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trips"
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="trips"
    )

    name = models.CharField(max_length=200)

    start_date = models.DateField()

    end_date = models.DateField()

    travelers = models.PositiveIntegerField(default=1)

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Itinerary(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="itinerary_items"
    )

    day_number = models.PositiveIntegerField()

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    start_time = models.TimeField(
        null=True,
        blank=True
    )

    end_time = models.TimeField(
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=300,
        blank=True
    )

    estimated_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.trip.name} - Day {self.day_number}"