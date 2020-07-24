from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse


# view for index
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


# view for flight
def flight(request, flight_id):
    # here pk is the primary key we can also use id there
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    # when user submits the form
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        # this is the id of the passenger we would like to add
        passid = int(request.POST["passenger"])
        # getting the passenger
        passenger = Passenger.objects.get(pk=passid)
        # todo error checking, to check if the passenger is present or the flight is present
        # adding the passenger to the flight
        passenger.flights.add(flight)
        # redirecting to that particular flight route
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
