# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..loginapp.models import Users
from .models import Quote, Favorite

# Create your views here.
def index(request):
    if not 'user' in request.session or not request.session['user']:
        return redirect('/')

    else:
        user = Users.usersManager.filter(id = request.session['user'])
        user_favorites = Favorite.favoritesManager.filter(user = user)
        quotes = Quote.quotesManager.all()

        for favorite in user_favorites:
            quotes = quotes.exclude(id = favorite.quote_id)
        quotes = quotes

        context = {
        "quotes" : quotes,
        "name" : user.values_list("name", flat=True)[0],
        "favorites": Favorite.favoritesManager.filter(user=user)
        }
        return render(request, 'examapp/dashboard.html', context)

def quotes(request):
    if request.method == "POST":
        check = Quote.quotesManager.add(poster = request.session['user'], author = request.POST['author'], quote = request.POST['quote'])

        if not check[0]:
            for message in check[1]:
                messages.add_message(request, messages.ERROR, message)
            return redirect('/add')

        return redirect('/quotes')

    else:
        return redirect('/quotes')

def favorites(request, id):
    Favorite.favoritesManager.add(quote = id, user=request.session['user'])
    return redirect('/quotes')

def remove(request, id):
    Favorite.favoritesManager.remove(id=id)
    return redirect('/quotes')

def show_user(request, id):
    poster = Users.usersManager.filter(id = id)
    context = {
    "users" : poster,
    "num_quotes" : Quote.quotesManager.filter(poster = poster).count(),
    "quotes": Quote.quotesManager.filter(poster_id = id)
    }
    return render(request, 'examapp/showUser.html', context)
