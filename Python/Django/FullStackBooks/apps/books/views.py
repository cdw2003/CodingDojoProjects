# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Book

def index(request):
    context = {
    "books" : Book.objects.all()
    }
    return render(request, 'books/index.html', context)

def books(request):
    if request.method == "POST":
        Book.objects.create(title = request.POST['title'], author = request.POST['author'], category = request.POST['category'])
        return redirect('/')
    else:
        return redirect('/')
