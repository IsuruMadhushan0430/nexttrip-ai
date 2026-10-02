from django.db import models

# Create your models here.

from destinations.models import Destination


class Hotel(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="hotels"
    )

    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    address = models.TextField()

    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="hotels/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name