from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user.models import User
from user.api.serializers import User_Serializer

#class view için modüller
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
#class method ile requestleri karşılama


class User_filter(APIView):
    def get(self,request):
        user_instance = User.objects.all()
        serializer=User_Serializer(user_instance,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class User_Detail(APIView):

    def get_object(self,request,id):
        user_instance= get_object_or_404(User,pk=id)
        return user_instance
    
    
    def get(self,request,id):
        
        user_instance = self.get_object(request,id=id)
        serializer = User_Serializer(user_instance)
        return Response(serializer.data)
    
    
    def put(self,request,id):
        user_instance = self.get_object(request,id=id)
        serializer = User_Serializer(user_instance,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        user_instance = self.get_object(request, id=id)
        serializer = User_Serializer(user_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,id):
        user_instance = self.get_object(request,id=id)
        user_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


