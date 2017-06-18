# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def noNinjas(request):
    return render(request, 'ninjas/index.html')

def helloNinjas(request):
    return render(request, 'ninjas/fourninjas.html')

def colorNinjas(request, color):
    name = ""
    context = {
        "color" : color,
    }
    if color == "blue":
        return render(request, 'ninjas/ninjacolor.html', context)
    elif color == "orange":
        return render(request, 'ninjas/ninjacolor.html', context)
    elif color == "purple":
        return render(request, 'ninjas/ninjacolor.html', context)
    elif color == "red":
        return render(request, 'ninjas/ninjacolor.html', context)
    else:
        return render(request, 'ninjas/ninjaerror.html', context)
