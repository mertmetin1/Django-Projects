from django.shortcuts import render
from .models import Category,Movies


"""kategori_liste=["macera","romantik","dram","bilim kurgu"]
film_liste= [
    
    {
        "id":1,
        "film_adi":"film1",
        "aciklama":"film1 acıklama",
        "resim":"1.jpg",
        "anasayfa":True   
    },
   
    {    
        "id":2,
        "film_adi":"film2",
        "aciklama":"film2 acıklama",
        "resim":"2.jpg",
        "anasayfa":False  
    },
         
    {     
        "id":3,
        "film_adi":"film3",
        "aciklama":"film3 acıklama",
        "resim":"3.jpg",
        "anasayfa":True  
    },
       {    
        "id":4,
        "film_adi":"film4",
        "aciklama":"film4 acıklama",
        "resim":"4.jpg",
        "anasayfa":False  
    },
]
"""
def home(request):
    data={
        "kategoriler":Category.objects.all(),
        "filmler":Movies.objects.filter(anasayfa=True)   
    }
    return render(request,"index.html",data)
def movies(request):
    data={
        "kategoriler":Category.objects.all(),
        "filmler":Movies.objects.all()   
    }
    return render(request,"movies.html",data)



def moviesdetails(request,id):
    data={
        "movie":Movies.objects.get(id=id)
    }
    return render(request,"details.html",data)