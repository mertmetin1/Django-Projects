from rest_framework import mixins
from client.models import Client
from client.api.serializers import ClientSerializer, LoginClientSerializer,RegisterClientSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from client.api.permissions import IsOwnerOrReadOnly


class ClientViewSet(
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset =Client.objects.filter()
    serializer_class=ClientSerializer
    permission_classes=[IsOwnerOrReadOnly]
    
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class RegisterClientViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = RegisterClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    


class LoginClientViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = LoginClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        if user is None:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)