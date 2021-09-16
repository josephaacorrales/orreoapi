from django.contrib.auth.models import User
from django.db import models

class Gw2Key(models.Model):
    key = models.CharField(max_length=72)
    name = models.CharField(max_length=72)
    author = models.ForeignKey(User, related_name='gw2keys', on_delete=models.CASCADE)
