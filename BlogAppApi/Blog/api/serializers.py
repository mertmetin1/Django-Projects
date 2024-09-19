#Blog/api/serializers.py

from rest_framework import serializers
from Blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):


    #blog_is_active=serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Blog
        fields='__all__'
        
        
    def get_fields(self):
        fields = super().get_fields()

        # Get the request object from the context
        request = self.context.get('request')

        # If the user is not a superuser, make certain fields read-only or hidden
        if not request.user.is_superuser:
            fields['blog_isGenByAi'].read_only = True
            # Add other fields to be read-only or hidden here
            # fields.pop('some_field')  # To hide a field
            fields['blog_owner'].read_only = True
            # Add other fields to be read-only or hidden here
            
        return fields
        