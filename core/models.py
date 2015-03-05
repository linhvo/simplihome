from django.db import models

class User(models.Model):
    user_name = models.CharField()
    password = models.CharField()
    token = models.CharField()