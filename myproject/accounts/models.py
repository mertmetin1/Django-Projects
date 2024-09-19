# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
validate_phone_code = RegexValidator(
    regex=r'^\d{1,5}$', 
    message="Phone code must be numeric and between 1 to 5 digits."
)
validate_phone_number = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', 
    message="Phone number must be between 9 and 15 digits and may include a '+'."
)



class Client(AbstractUser):

    email = models.EmailField(unique=True, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_code = models.CharField(
        max_length=5, 
        validators=[validate_phone_code], 
        blank=True, 
        null=True
    )
    phone_number = models.CharField(
        max_length=15, 
        validators=[validate_phone_number], 
        blank=True, 
        null=True
    )
    organization = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    joined = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name_plural='Clients'

    def __str__(self):
        return f"{self.username}"
