from rest_framework import serializers
from client.models import Client
from rest_framework.authtoken.models import Token

class ClientSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model = Client
        fields='__all__'
        #fields = ['id','password','username', 'first_name', 'last_name', 'email', 'country', 'bio', 'organization', 'phone_code', 'phone_number']


    def get_fields(self):
        fields = super().get_fields()

        # Get the request object from the context
        request = self.context.get('request')

        # If the user is not a superuser, make certain fields read-only or hidden
        if not request.user.is_superuser:
            fields['password'].read_only = True
            fields['is_superuser'].read_only = True
            fields['username'].read_only = True
            fields['is_staff'].read_only = True
            fields['is_active'].read_only = True
            fields['email'].read_only = True
            fields['phone_number'].read_only = True
            fields['phone_code'].read_only = True
            fields['is_verified'].read_only = True
            fields['groups'].read_only = True
            fields['user_permissions'].read_only = True
           

        return fields  



from rest_framework import serializers
from client.models import Client
from rest_framework.authtoken.models import Token

class RegisterClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ['id','password','username',  'first_name', 'last_name', 'email', 'country', 'bio', 'organization', 'phone_code', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
            'phone_code': {'write_only': True},
            'phone_number': {'write_only': True},
            'username':{'write_only': True}
        }
    def create(self, validated_data):
        user = super().create(validated_data)
        # Handle user creation for Client model
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.get_or_create(user=user)
        return user


from rest_framework import serializers

class LoginClientSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return data
