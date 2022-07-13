from django.contrib.auth.models import User
from django.db import models


class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(min_length=6)
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=10)
    email = models.EmailField()
    photo = models.ImageField()
    active = models.BooleanField(default=False)



