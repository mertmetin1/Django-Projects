#Blog/api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


from Blog.models import Blog
from Blog.api.serializers import BlogSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins,viewsets
from rest_framework.filters import SearchFilter
from Blog.api.permissions import OwnerOrReadOnly,VerifiedBloggerPermission

from User.models import Blogger



class BlogViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset =Blog.objects.filter(blog_is_active=True,blog_IsDeleted=False, blog_owner__blogger_IsVerified=True)
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,OwnerOrReadOnly,VerifiedBloggerPermission]
    
    def perform_create(self, serializer):
        # Fetch the Blogger instance related to the current user
        blogger = Blogger.objects.get(blogger_user=self.request.user)
        serializer.save(blog_owner=blogger)



    def perform_destroy(self, instance):
        instance.delete()