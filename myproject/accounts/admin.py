from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_code', 'phone_number', 'organization', 'is_verified', 'joined')


