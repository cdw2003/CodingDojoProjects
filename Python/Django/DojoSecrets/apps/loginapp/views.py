# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

# Create your views here.
def index(request):
    return render(request, 'loginapp/index.html')

def register(request):
    check = Users.usersManager.add(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['pwconfirm'])
    print check

    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')

    else:
        request.session['first_name'] = request.POST['first_name']
        request.session['email'] = request.POST['email']
        request.session['user'] = check[1].id
        return redirect('/secrets')

def login(request):
    check = Users.usersManager.login(request.POST['email'], request.POST['password'])

    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')

    else:
        request.session['email'] = request.POST['email']
        request.session['user'] = check[1][0].id
        return redirect('/secrets')

def logout(request):
    request.session.clear()
    return redirect("/")
