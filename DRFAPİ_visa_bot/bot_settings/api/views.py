from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from bot_settings.models import Bot_Setting
from bot_settings.api.serializers import Bot_Setting_Serializer

#class view için modüller
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
#class method ile requestleri karşılama
class Bot_Setting_filter(APIView):
    def get(self,request):
        Bot_Setting_instance = Bot_Setting.objects.all()
        serializer=Bot_Setting_Serializer(Bot_Setting_instance,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = Bot_Setting_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class Bot_Setting_Detail(APIView):

    def get_object(self,request,id):
        Bot_Setting_instance= get_object_or_404(Bot_Setting,pk=id)
        return Bot_Setting_instance
    
    
    def get(self,request,id):
        
        Bot_Setting_instance = self.get_object(request,id=id)
        serializer = Bot_Setting_Serializer(Bot_Setting_instance)
        return Response(serializer.data)
    
    
    def put(self,request,id):
        Bot_Setting_instance = self.get_object(request,id=id)
        serializer = Bot_Setting_Serializer(Bot_Setting_instance,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        Bot_Setting_instance = self.get_object(request, id=id)
        serializer = Bot_Setting_Serializer(Bot_Setting_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,id):
        Bot_Setting_instance = self.get_object(request,id=id)
        Bot_Setting_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        





#Function method yöntemi ile requestleri karşılama

"""

@api_view(['GET','POST'])
def Bot_Setting_Filter(request):
    if request.method == 'GET':
        Bot_Settings=Bot_Setting.objects.filter()
        Serializer=Bot_Setting_Serializer(Bot_Settings,many=True) #istek sonucu veritabnaından gelen veri instance mı yoksa querry set mi dikkat et eğer öyleyse many=true ekle
        return Response(Serializer.data)
    elif request.method == 'POST':
        Serializer =Bot_Setting_Serializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data ,status= status.HTTP_201_CREATED)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET','PUT','DELETE'])
def Bot_Setting_Detail(request,id):
    try:
        
        bot_setting_instance=Bot_Setting.objects.get(pk=id)
    except Bot_Setting.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND )
    
    
    if request.method =='GET':
        serializer =Bot_Setting_Serializer(bot_setting_instance)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        Serializer =Bot_Setting_Serializer(bot_setting_instance,data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method =='DELETE':
        bot_setting_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""
    