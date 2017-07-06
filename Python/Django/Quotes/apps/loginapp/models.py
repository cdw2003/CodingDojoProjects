from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
import datetime
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d]{8,}$')

class UsersManager(models.Manager):
    def add(self, name, alias, email, birthday, password, pwconfirm):
        messages = []
        invalid = False
        if len(name) < 1:
            invalid = True
            messages.append("Name is required!")

        if len(name) < 3:
            invalid = True
            messages.append("Name must be at least three characters!")

        if name.isalpha() == False:
            invalid = True
            messages.append("Name must only contain letters!")

        if len(alias) < 1:
            invalid = True
            messages.append("Alias is required!")

        if len(alias) < 3:
            invalid = True
            messages.append("Alias must be at least three characters!")

        if len(email) < 1:
            invalid = True
            messages.append("Email is required!")

        if not EMAIL_REGEX.match(email):
            invalid = True
            messages.append("Email must be in a valid format!")

        if datetime.datetime.strptime(birthday,'%Y-%m-%d') >= datetime.datetime.now():
            invalid = True
            messages.append("Birth date must be in the past!")

        if len(password) < 1:
            invalid = True
            messages.append("Password is required!")

        if len(password) < 8:
            invalid = True
            messages.append("Password must be at least 8 characters!")

        if not PASSWORD_REGEX.match(password):
            invalid = True
            messages.append("Password must contain at least one number, one uppercase and one lowercase letter!")

        if password != pwconfirm:
            invalid = True
            messages.append("Password and password confirm must match!")

        if invalid:
            return (False, messages)

        else:
            hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = Users.usersManager.create(name = name, alias = alias, email = email, birthday = birthday, password = hash)
            return (True, user)

    def login(self, email, password):
        messages = []
        invalid = False
        if len(email) < 1:
            invalid = True
            messages.append("You must enter an email address!")

        if len(password) < 1:
            invalid = True
            messages.append("You must enter a password!")

        if invalid:
            return (False, messages)

        else:
            user = Users.usersManager.filter(email = email)

            if len(user) == 0:
                messages.append('The email submitted does not match our records.')
                return (False, messages)

            elif bcrypt.checkpw(password.encode(), user[0].password.encode()):
                return (True, user[0])

            else:
                messages.append('Incorrect password!')
                return (False, messages)


class Users(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    birthday = models.DateTimeField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    usersManager = UsersManager()
