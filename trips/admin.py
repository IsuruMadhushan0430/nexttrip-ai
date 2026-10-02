from django.contrib import admin

# Register your models here.

from .models import Trip, Itinerary

admin.site.register(Trip)
admin.site.register(Itinerary)