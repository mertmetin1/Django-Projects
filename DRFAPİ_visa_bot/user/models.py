from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    isAdmin=models.BooleanField(default=False)


    def __str__(self):
        return self.username