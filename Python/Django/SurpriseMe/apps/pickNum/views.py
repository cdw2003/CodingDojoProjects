# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
values = ['ice cream', 'pizza', 'tacos', 'wine', 'cheese', 'yogurt', 'cherries', 'peanuts', 'macaroni', 'eggs', 'avocados', 'pasta', 'sandwiches', 'turkey', 'broccoli', 'pancakes', 'grits', 'corn bread', 'collard greens', 'kale']
# Create your views here.
def index(request):
    return render(request, 'pickNum/index.html')

def processNumber(request):
    if request.method == "POST":
        request.session['number'] = request.POST['number']
        return redirect('/results')
    else:
        return redirect('/')

def showInfo(request):
    words = []
    random.shuffle(values, random.random)
    if int(request.session['number']) <= 20:
        for i in range (0, int(request.session['number'])):
            words.append(values[i])
        context = {
            "Item": words
        }
    else:
        return redirect('/')
    return render(request, 'pickNum/results.html', context)
