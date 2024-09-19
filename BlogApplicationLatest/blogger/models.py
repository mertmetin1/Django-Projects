from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models



class Blogger(AbstractUser):
    
    email = models.EmailField(unique=True, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_code = models.CharField(
        max_length=5, 
        blank=True, 
        null=True
    )
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True
    )
    organization = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    joined = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name_plural='Bloggers'

    def __str__(self):
        return f"{self.username}"
