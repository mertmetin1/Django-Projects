from rest_framework import serializers
from user.models import User



#model serializer (dinamik serializer oluşturma yöntemi)
class User_Serializer(serializers.ModelSerializer):
    class Meta:        
        model=User
        fields='__all__'