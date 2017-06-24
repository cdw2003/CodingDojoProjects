from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def add(self, first_name, last_name, email, password, pwconfirm):
        messages = []
        invalid = False
        if len(first_name) < 1:
            invalid = True
            messages.append("First name is required!")

        if len(first_name) < 2:
            invalid = True
            messages.append("First name must be at least two characters!")

        if first_name.isalpha() == False:
            invalid = True
            messages.append("First name must only contain letters!")

        if len(last_name) < 1:
            invalid = True
            messages.append("Last name is required!")

        if len(last_name) < 2:
            invalid = True
            messages.append("Last name must be at least two characters!")

        if last_name.isalpha() == False:
            invalid = True
            messages.append("Last name must only contain letters!")

        if len(email) < 1:
            invalid = True
            messages.append("Email is required!")

        if not EMAIL_REGEX.match(email):
            invalid = True
            messages.append("Email must be in a valid format!")

        if len(password) < 1:
            invalid = True
            messages.append("Password is required!")

        if len(password) < 8:
            invalid = True
            messages.append("Password must be at least 8 characters!")

        if password != pwconfirm:
            invalid = True
            messages.append("Password and password confirm must match!")

        if invalid:
            return (False, messages)

        else:
            user = Users.usersManager.create(first_name = first_name, last_name = last_name, email = email, password = password)
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
            user = Users.usersManager.filter(email = email, password = password)

            if len(user) == 0:
                invalid = True
                messages.append('The email and/or password you submitted does not match our records.')
                return (False, messages)

            elif len(user) > 0:
                return (True, user)

class Users(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    usersManager = UsersManager()
