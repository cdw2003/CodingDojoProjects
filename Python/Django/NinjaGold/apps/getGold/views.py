# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random
# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['results'] = []
    return render(request, 'getGold/index.html')

def points(request):
    message = ''
    if request.method == "POST":
        request.session['location'] = request.POST['building']
        if request.session['location'] == "farm":
            gold = random.randrange(10, 21)
            request.session['gold'] += gold
            message = "Earned {} golds from the {}". format(gold, request.session['location']) + "\n"
        elif request.session['location'] == "cave":
            gold = random.randrange(5, 11)
            request.session['gold'] += gold
            message = "Earned {} golds from the {}". format(gold, request.session['location']) + "\n"
        elif request.session['location'] == "house":
            gold = random.randrange(2, 6)
            request.session['gold'] += gold
            message = "Earned {} golds from the {}". format(gold, request.session['location']) + "\n"
        elif request.session['location'] == "casino":
            gold = random.randrange(-50, 51)
            if gold > 0:
                request.session['gold'] += gold
                message = "Earned {} golds from the {}". format(gold, request.session['location']) + "\n"
            elif gold < 0:
                request.session['gold'] += gold
                message = "Entered a casino and lost {}...Ouch.". format(gold) + "\n"
        time = datetime.strftime(datetime.now(), '(%H:%M  %m/%d/%Y)')
        if request.session['gold'] <= 0:
            message = "Game over."
        message += time
        request.session['results'].append(message)
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
