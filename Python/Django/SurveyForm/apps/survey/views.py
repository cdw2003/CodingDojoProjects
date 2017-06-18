# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def processForm(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['dojo_location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['number'] += 1
        return redirect('/results')
    else:
        return redirect('/')

def showInfo(request):
    return render(request, 'survey/results.html')
