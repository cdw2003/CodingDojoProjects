# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Count
import datetime
from django.utils.timesince import timesince
from django.contrib import messages
from ..loginapp.models import Users
from .models import Book, Review

# Create your views here.
def index(request):
    if not 'user' in request.session or not request.session['user']:
        return redirect('/')

    else:
        user = Users.usersManager.filter(id = request.session['user'])
        context = {
        "books" : Book.booksManager.all().order_by("-created_at")[0:3],
        "name" : user.values_list("name", flat=True)[0],
        "reviews": Review.reviewsManager.all()
        }
        return render(request, 'booksapp/index.html', context)

def new_book(request):
    context = {
    "books" : Book.booksManager.all(),
    "authors" : Book.booksManager.all().values_list("author", flat=True)
    }
    return render(request, 'booksapp/addBook.html', context)

def add_book(request):
    check = Book.booksManager.add(title = request.POST['title'], author = request.POST['author'])
    check[1].save()
    check2 = Review.reviewsManager.add(content = request.POST['content'], rating = request.POST['rating'], user = request.session['user'], book = check[1].id)

    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/add_book')

    elif not check2[0]:
        for message in check2[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/add_book')

    else:
        return redirect('/books')

def show_books(request, id):
    books = Book.booksManager.get(id=id)
    reviews = Review.reviewsManager.filter(book_id=id)
    print reviews
    context = {
    "books": books,
    "reviews": reviews
    }
    return render(request, 'booksapp/showBook.html', context)

def reviews(request, id):
    Review.reviewsManager.add(content = request.POST['content'], rating = request.POST['rating'], user = request.session['user'], book=id)
    return redirect('/books')

def remove_review(request, id):
    Review.reviewsManager.remove(id=id)
    return redirect('/books')

def show_user(request, id):
    user = Users.usersManager.filter(id = id)
    context = {
    "users" : user,
    "reviews" : Review.reviewsManager.filter(user_id = id),
    "num_reviews" : Review.reviewsManager.filter(user = user).count()
    }
    return render(request, 'booksapp/showUser.html', context)
