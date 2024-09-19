from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import Client
from .serializers import ClientSerializer, AuthTokenSerializer, RegisterSerializer



class RegisterViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': ClientSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for logging in users.
    """
    def create(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': ClientSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
