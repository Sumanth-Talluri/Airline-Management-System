from django.contrib import admin
from .models import Airport, Flight, Passenger


# customizing the admin page of FLight
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


# customizing the admin page of Passenger
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
