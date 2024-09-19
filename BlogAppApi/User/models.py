
#User/models.py
from django.db import models
from User.api.validators import validate_phone_number,validate_phone_code
from django.contrib.auth.models import User




class Blogger(models.Model):
    blogger_user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="blogOwnerUser")
    blogger_phone_code = models.CharField(max_length=5, validators=[validate_phone_code], blank=True, null=True)
    blogger_phone_number = models.CharField(validators=[validate_phone_number], max_length=15, blank=True, null=True)
    #blogger_IsActive = models.BooleanField(default=True)
    blogger_organization = models.CharField(max_length=100, blank=True,null=True)
    blogger_bio=models.CharField(max_length=500,blank=True,null=True)
    blogger_IsVerified = models.BooleanField(default=False)
    #keywords = models.JSONField(blank=True, default=list)
    blogger_joined= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Bloggers'
        
    def __str__(self) :
        return str(self.blogger_user.username)