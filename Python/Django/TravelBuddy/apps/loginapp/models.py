from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
import bcrypt
PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d]{8,}$')

class UsersManager(models.Manager):
    def add(self, name, username, password, pwconfirm):
        messages = []
        invalid = False
        if len(name) < 1:
            invalid = True
            messages.append("Name is required!")

        if len(name) < 3:
            invalid = True
            messages.append("Name must be at least three characters!")

        if len(username) < 1:
            invalid = True
            messages.append("Username is required!")

        if len(username) < 3:
            invalid = True
            messages.append("Username must be at least three characters!")

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
            user = Users.usersManager.create(name = name, username = username, password = hash)
            return (True, user)

    def login(self, username, password):
        messages = []
        invalid = False
        if len(username) < 1:
            invalid = True
            messages.append("You must enter a username!")

        if len(password) < 1:
            invalid = True
            messages.append("You must enter a password!")

        if invalid:
            return (False, messages)

        else:
            user = Users.usersManager.filter(username = username)

            if len(user) == 0:
                messages.append('The username submitted does not match our records.')
                return (False, messages)

            elif bcrypt.checkpw(password.encode(), user[0].password.encode()):
                return (True, user[0])

            else:
                messages.append('Incorrect password!')
                return (False, messages)


class Users(models.Model):
    name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 45)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    usersManager = UsersManager()
