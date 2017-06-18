# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, "wordGenerate/index.html")

def createWord(request):
    word = ""

    for i in range(1, 15):
        randomLetter = random.choice('abcdefghijklmnopqrstuvwxyz')
        word += randomLetter
        print word

    if request.method == "POST":
        request.session['word'] = word
        request.session['count'] += 1
        return redirect('/')
    else:
        return redirect('/')
