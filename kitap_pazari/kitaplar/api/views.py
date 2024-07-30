from kitaplar.api.serializers import KitapSerializer,YorumSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from kitaplar.models import Kitap,Yorum
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import permissions
from kitaplar.api.permissions import IsAdminUserOrReadOnly,IsYorumSahibiOrReadOnly
from rest_framework.exceptions import ValidationError


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset =Kitap.objects.all()
    serializer_class =KitapSerializer
    permission_classes=[permissions.IsAuthenticated]
    # pagination_class = LargePagination


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView ):
    
    queryset =Kitap.objects.all()
    serializer_class =KitapSerializer 
    
    #standart permission classlar  
    #permission_classes=[permissions.IsAdminUser]
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    permission_classes=[permissions.IsAuthenticated]
    
    #kendi yaptığımız permisson classı
    #permission_classes=[IsAdminUserOrReadOnly]
    
    
class YorumCreateAPIView(generics.CreateAPIView):
    queryset =Yorum.objects.all()
    serializer_class =YorumSerializer
    permission_classes=[permissions.IsAuthenticated]
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        #path('kitaplar/<int:kitap_pk>/yorum_yap',api_views.YorumCreateAPIView.as_view(),name='yorum-yap'),
        kitap_pk=self.kwargs.get('kitap_pk')
        kitap=get_object_or_404(Kitap,pk=kitap_pk)
        
        
        kullanici=self.request.user
        yorumlar=Yorum.objects.filter(kitap=kitap,yorum_sahibi=kullanici)
        if yorumlar.exists():
            raise ValidationError('bir kitaba sadece 1 yorum yapabilriisniz')
        serializer.save(kitap=kitap,yorum_sahibi=kullanici)
            
            
            
            
            
class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Yorum.objects.all()
    serializer_class =YorumSerializer 
    permission_classes=[IsYorumSahibiOrReadOnly]


"""

class KitapListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset =Kitap.objects.all()
    serializer_class =KitapSerializer
    
    #listelemek
    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)

    #yaratmak
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    """
    
    