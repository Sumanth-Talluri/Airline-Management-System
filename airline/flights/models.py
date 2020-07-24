from django.db import models

# Create your models here.
# models are python classes which represent each table


# Airport model
class Airport(models.Model):
    # below are the rows for Airport tabel
    # there'll be a id row by default which is PK and AI
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    # this function will be called when you want to print the object
    def __str__(self):
        return f"{self.city} ({self.code})"


# Flight model
class Flight(models.Model):
    # below are the rows for Flight tabel
    # there'll be a id row by default which is PK and AI

    # origin and destination are a ForeignKey that references Airport table
    # CASCADE means if data is deleted in Airports table then it'll be deleted here too
    # related_name will establish the relationship so that we can reference in reverse too
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    # origin = models.CharField(max_length=64)
    # destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    # this function will be called when you want to print the object
    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"


# Passengers model
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # passengers have a many to many relationship with flights
    # blank is True as there can be passengers with no flights
    flights = models.ManyToManyField(
        Flight, blank=True, related_name="passengers")

    # this function will be called when you want to print the object
    def __str__(self):
        return f"{self.first} {self.last}"
