from rest_framework import serializers
from client.models import Client



#model serializer (dinamik serializer oluşturma yöntemi)
class Client_Serializer(serializers.ModelSerializer):
    class Meta:        
        model=Client
        fields='__all__'