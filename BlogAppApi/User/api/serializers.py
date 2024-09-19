#User/api/serializers.py

from rest_framework import serializers

from User.models import Blogger
from User.api.validators import validate_phone_number,validate_phone_code
from Blog.api.serializers import BlogSerializer
from rest_framework.reverse import reverse

        
class BloggerSerializer(serializers.ModelSerializer):

    
    
    blogger_user=serializers.StringRelatedField()
    
    
    #blogger_username = serializers.ReadOnlyField(source='blogger_user.name')
    blogger_email = serializers.ReadOnlyField(source='blogger_user.email')
    
    # Check if valid data is provided and set blogger_IsVerified to True
    blogger_phone_number = serializers.CharField(validators=[validate_phone_number])
    blogger_phone_code = serializers.CharField(validators=[validate_phone_code])
    blogger_IsVerified =serializers.BooleanField()
    blogger_organization = serializers.CharField(min_length=3,max_length=100 )
    blogger_bio = serializers.CharField(min_length=10,max_length=500)
    blogs = serializers.SerializerMethodField()
    # #blogModel = BlogSerializer(many=True, read_only=True)  # Nested serializer to include blogs
    # blogs = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='blog-detail',source='blogModel')

    class Meta:
        model =Blogger
        fields='__all__'
        exclude=[]
    
    def get_fields(self):
        fields = super().get_fields()

        # Get the request object from the context
        request = self.context.get('request')

        # If the user is not a superuser, make certain fields read-only or hidden
        if not request.user.is_superuser:
            fields['blogger_IsVerified'].read_only = True
            fields['blogger_user'].read_only = True

            fields['blogger_email'].read_only = True
            
        return fields    

    def update(self, instance, validated_data):

        validated_data['blogger_IsVerified'] = True
        
        return super().update(instance, validated_data)


    def get_blogs(self, obj):
        request = self.context.get('request')
        blogs = obj.blogModel.filter(blog_IsDeleted=False, blog_is_active=True)
        return [reverse('blog-detail', args=[blog.pk], request=request) for blog in blogs]

    