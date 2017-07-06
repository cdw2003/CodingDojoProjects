# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib import messages
from ..loginapp.models import Users

# Create your models here.
class QuotesManager(models.Manager):
    def add(self, poster, author, quote):
        messages = []
        if len(author) == 0:
            messages.append("You must enter the quote's author!")
            return (False, messages)

        if len(quote) == 0:
            messages.append("You must enter a quote!")
            return (False, messages)

        if len(author) < 3:
            messages.append("The quote's author must be at least 3 characters!")
            return (False, messages)

        if len(quote) < 10:
            messages.append("The quote must be at least 10 characters!")
            return (False, messages)

        else:
            quote = Quote.quotesManager.create(poster_id = poster, author = author, quote = quote)
            return (True, quote)

class FavoritesManager(models.Manager):
    def add(self, quote, user):
        check = Favorite.favoritesManager.filter(quote_id=quote, user_id = user)
        if len(check) == 0:
            favorite = Favorite.favoritesManager.create(quote_id = quote, user_id = user)
            return favorite

    def remove(self, id):
        favorite = Favorite.favoritesManager.filter(quote_id=id)
        favorite.delete()

class Quote(models.Model):
    poster = models.ForeignKey(Users, related_name = "poster")
    author = models.CharField(max_length = 255)
    quote = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    quotesManager = QuotesManager()

class Favorite(models.Model):
    quote = models.ForeignKey(Quote, related_name = "quotes")
    user = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    favoritesManager = FavoritesManager()
