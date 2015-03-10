from django.db import models
from django.contrib.auth.models import User

class NestUser(models.Model):
    user = models.ForeignKey(User, related_name='nest_users')
    nest_token = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)


class SimplisafeUser(models.Model):
    user = models.ForeignKey(User, related_name='simplisafe_users')
    email = models.EmailField()
    password = models.CharField(max_length=40)
    simplisafe_token = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)




