#User/api/views.py

from User.models import Blogger
from User.api.serializers import BloggerSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser
from User.api.permissions import OwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
class BloggerViewSet(
                   #mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset =Blogger.objects.filter()
    serializer_class=BloggerSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,OwnerOrReadOnly]



        
        
