from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    visa = models.BooleanField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # Oluşturulma tarihi
    updated_at = models.DateTimeField(auto_now=True)  # Değiştirilme tarihi

    def __str__(self):
        return self.email
