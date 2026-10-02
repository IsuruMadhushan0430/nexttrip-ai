from django.contrib import admin

# Register your models here.

from .models import Destination, Attraction


admin.site.register(Destination)
admin.site.register(Attraction)