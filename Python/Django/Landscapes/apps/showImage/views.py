# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, 'showImage/index.html')

def showImage(request, number):
    count = 0
    show = "one"
    random1 = random.randint(1,8)
    if int(number) <= 50:
        for i in range(2,50):
            if int(number) % i == 0:
                count += 1

        if count == 1:
            image = "random"
            if random1 == 1:
                show = "one"
            if random1 == 2:
                show = "two"
            if random1 == 3:
                show = "three"
            if random1 == 4:
                show = "four"
            if random1 == 5:
                show = "five"
            if random1 == 6:
                show = "six"
            if random1 == 7:
                show = "seven"
            if random1 == 8:
                show = "eight"

        elif int(number) <= 10:
            image = "snow"

        elif int(number) > 10 and int(number) <= 20:
            image = "desert"

        elif int(number) > 20 and int(number) <= 30:
            image = "forest"

        elif int(number) > 30 and int(number) <= 40:
            image = "vineyard"

        elif int(number) > 40 and int(number) <= 50:
            image = "tropical"

        context = {
            "number" : number,
            "image": image,
            "show": show
        }
        return render(request, 'showImage/image.html', context)

    else:
        return redirect('/')
