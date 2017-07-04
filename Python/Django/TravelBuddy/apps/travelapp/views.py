# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..loginapp.models import Users
from .models import Trip, UserTrip
# Create your views here.

def index(request):
    if not 'user' in request.session or not request.session['user']:
        return redirect('/')

    else:
        user = Users.usersManager.filter(id = request.session['user'])
        usertrips = UserTrip.userTripsManager.filter(traveler = request.session['user'])
        all_trips = Trip.tripsManager.all().exclude(planner = request.session['user'])

        for usertrip in usertrips:
            all_trips = all_trips.exclude(id = usertrip.trip_id)
        othertrips = all_trips

        context = {
        "trips" : usertrips,
        "name" : user.values_list("name", flat=True)[0],
        "othertrips" : othertrips
        }
        return render(request, 'travelapp/dashboard.html', context)

def add_trip(request):
    return render(request, 'travelapp/addplan.html')

def new_trip(request):
    check = Trip.tripsManager.add(planner = request.session['user'], destination = request.POST['destination'], description = request.POST['description'], date_from = request.POST['date_from'], date_to = request.POST['date_to'])

    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/add_trip')

    else:
        UserTrip.userTripsManager.join(trip = check[1].id, traveler = request.session['user'])
        return redirect('/schedule')

def join_trip(request, id):
    UserTrip.userTripsManager.join(trip = id, traveler = request.session['user'])
    return redirect('/schedule')

def destination(request, id):
    trips = Trip.tripsManager.filter(id = id)
    travelers = UserTrip.userTripsManager.filter(trip = id).exclude(traveler = trips.values_list("planner_id"))
    context = {
    "trips" : trips,
    "travelers" : travelers,
    }
    return render(request, 'travelapp/destination.html', context)
