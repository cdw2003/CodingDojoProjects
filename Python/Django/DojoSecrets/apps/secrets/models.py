# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..loginapp.models import Users

# Create your models here.
class SecretsManager(models.Manager):
    def post(self, content, user):
        messages = []
        if len(content) == 0:
            messages.append("Secrets can not be blank!")
            return (False, messages)

        elif len(content) > 0:
            secret = Secrets.secretsManager.create(content = content, user_id = user)
        return (True, secret)

    def remove(self, id):
        secret = Secrets.secretsManager.filter(id=id)
        secret.delete()

class LikesManager(models.Manager):
    def like(self, user, secret):
        check = Likes.likesManager.filter(user_id=user, secret_id = secret)
        if len(check) == 0:
            like = Likes.likesManager.create(user_id = user, secret_id = secret)
            return like

class Secrets(models.Model):
    content = models.TextField(max_length = 500)
    user = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    secretsManager = SecretsManager()

class Likes(models.Model):
    secret = models.ForeignKey(Secrets, related_name = "all_likes")
    user = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    likesManager = LikesManager()
