from django.db import models

# Create your models here.

from trips.models import Trip


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ("hotel", "Hotel"),
        ("food", "Food"),
        ("transport", "Transport"),
        ("activity", "Activity"),
        ("shopping", "Shopping"),
        ("other", "Other"),
    ]

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.description