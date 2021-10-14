from django.db import models

class User(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
