# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib import messages
from ..loginapp.models import Users

# Create your models here.

class TripsManager(models.Manager):
    def add(self, planner, destination, description, date_from, date_to):
        messages = []
        if len(destination) == 0:
            messages.append("You must enter a destination!")
            return (False, messages)

        if len(description) == 0:
            messages.append("You must enter a description for your destination!")
            return (False, messages)

        if len(date_from) == 0:
            messages.append("You must enter a start date for your trip!")
            return (False, messages)

        if len(date_to) == 0:
            messages.append("You must enter an end date for your trip!")
            return (False, messages)

        if datetime.datetime.strptime(date_from,'%Y-%m-%d') <= datetime.datetime.now():
            messages.append("Trip start date must be in the future!")
            return (False, messages)

        if datetime.datetime.strptime(date_to,'%Y-%m-%d') <= datetime.datetime.now():
            messages.append("Trip end date must be in the future!")
            return (False, messages)

        if date_to < date_from:
            messages.append("Trip start date must be before end date!")
            return (False, messages)

        else:
            trip = Trip.tripsManager.create(planner_id = planner, destination = destination, description = description, date_from = date_from, date_to = date_to)
            return (True, trip)

class UserTripsManager(models.Manager):
    def join(self, trip, traveler):
        check = UserTrip.userTripsManager.filter(trip_id = trip, traveler_id = traveler)
        if len(check) == 0:
            usertrip = UserTrip.userTripsManager.create(trip_id= trip, traveler_id = traveler)
            return (True, usertrip)

class Trip(models.Model):
    planner = models.ForeignKey(Users, related_name = "planner")
    destination = models.CharField(max_length = 255)
    description = models.TextField(max_length = 2000)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    tripsManager = TripsManager()

class UserTrip(models.Model):
    trip = models.ForeignKey(Trip)
    traveler = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userTripsManager = UserTripsManager()
