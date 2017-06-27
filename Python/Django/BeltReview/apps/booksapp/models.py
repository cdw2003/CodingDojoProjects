# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from ..loginapp.models import Users

# Create your models here.
class BooksManager(models.Manager):
    def add(self, title, author):
        messages = []
        if len(title) == 0:
            messages.append("You must enter a book title!")
            return (False, messages)

        if len(author) == 0:
            messages.append("You must enter or select an author!")
            return (False, messages)

        else:
            book = Book.booksManager.create(title = title, author = author)
            return (True, book)

class ReviewsManager(models.Manager):
    def add(self, content, rating, user, book):
        messages = []
        if len(content) == 0:
            messages.append("Reviews can not be blank!")
            return (False, messages)

        elif len(content) > 0:
            review = Review.reviewsManager.create(content = content, rating = rating, user_id = user, book_id = book)
        return (True, review)

    def remove(self, id):
        review = Review.reviewsManager.filter(id=id)
        review.delete()

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    booksManager = BooksManager()

class Review(models.Model):
    content = models.TextField(max_length = 2000)
    rating = models.IntegerField()
    user = models.ForeignKey(Users)
    book = models.ForeignKey(Book, related_name = "book")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    reviewsManager = ReviewsManager()
