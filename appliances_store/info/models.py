from django.db import models


class Users(models.Model):
    name = models.TextField(max_length=20, blank=True)
    surname = models.TextField(max_length=20, blank=True)
    email = models.EmailField(max_length=50)
    telephone = models.IntegerField()
    password = models.TextField(max_length=10)


