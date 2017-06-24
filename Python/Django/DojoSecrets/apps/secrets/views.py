from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Count
import datetime
from django.utils.timesince import timesince
from ..loginapp.models import Users
from .models import Secrets, Likes


def index(request):
    if not 'user' in request.session or not request.session['user']:
        return redirect('/')

    else:
        user = Users.usersManager.filter(id = request.session['user'])
        context = {
        "secrets" : Secrets.secretsManager.all().order_by("created_at").annotate(Count('all_likes')),
        "name" : user.values_list("first_name", flat=True)[0],
        "likes": Likes.likesManager.all()
        }
        return render(request, 'secrets/index.html', context)

def secrets(request):
    if request.method == "POST":
        Secrets.secretsManager.post(content = request.POST['content'], user = request.session['user'])
        return redirect('/secrets')
    else:
        return redirect('/secrets')

def like(request, id):
    Likes.likesManager.like(user = request.session['user'], secret=id)
    return redirect('/secrets')

def remove(request, id):
    Secrets.secretsManager.remove(id=id)
    return redirect('/secrets')

def popular(request):
    context = {
    "secrets" : Secrets.secretsManager.all().annotate(num_likes = Count('all_likes')).order_by('-num_likes'),
    "likes": Likes.likesManager.all()
    }
    return render(request, 'secrets/popular.html', context)
