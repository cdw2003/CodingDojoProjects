# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    context = {
        "day": datetime.datetime.now().strftime('%b ''%d, ''%Y'),
        "time": datetime.datetime.now().strftime('%I:''%M ''%p')
    }

    return render(request, "TimeDisplay/index.html", context)
