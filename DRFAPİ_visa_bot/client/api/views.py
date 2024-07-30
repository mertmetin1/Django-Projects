from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from client.models import Client
from client.api.serializers import Client_Serializer

#class view için modüller
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
#class method ile requestleri karşılama


class Client_filter(APIView):
    def get(self,request):
        client_instance = Client.objects.all()
        serializer=Client_Serializer(client_instance,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = Client_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class Client_Detail(APIView):

    def get_object(self,request,id):
        client_instance= get_object_or_404(Client,pk=id)
        return client_instance
    
    
    def get(self,request,id):
        
        client_instance = self.get_object(request,id=id)
        serializer = Client_Serializer(client_instance)
        return Response(serializer.data)
    
    
    def put(self,request,id):
        client_instance = self.get_object(request,id=id)
        serializer = Client_Serializer(client_instance,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, id):
        client_instance = self.get_object(request, id=id)
        serializer = Client_Serializer(client_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        client_instance = self.get_object(request,id=id)
        client_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


