# User/api/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from User.models import Blogger

@receiver(post_save, sender=User)
def create_blogger(sender, instance, created, **kwargs):
    
    print(instance.username, '__created: ',created)
    
    if created:
        Blogger.objects.create(blogger_user=instance)
