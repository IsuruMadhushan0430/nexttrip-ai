from django.db import models

# Create your models here.

from destinations.models import Destination


class Restaurant(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="restaurants"
    )

    name = models.CharField(max_length=200)

    cuisine = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    address = models.TextField()

    average_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="restaurants/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name