from django.shortcuts import render
from .models import *
from user.models import *

# Create your views here.
def anaSayfa(request):
    return render(request,"index.html")
def hesap(request):
    return render(request,"hesap.html")
def browse_index(request):
    filmler=Movies.objects.all()
    search_movie=""
    if request.GET.get("search_movie"):
        search_movie=request.GET.get("search_movie")
        filmler=filmler.filter(filmismi__icontains=search_movie)


    context={}
    # print("izleyen"+Izlenenler.objects.get(user=request.user))
    try:
        izleyen=Izlenenler.objects.get(user=request.user)
        izlenen=izleyen.izlenen.all()
        context={
            "izlenen":izlenen,
            "filmler":filmler,
            "search_movie":search_movie
        }
        return render(request,"browse-index.html",context)
    except:

        context={
          "filmler":filmler, 
          "search_movie":search_movie
          }
        return render(request,"browse-index.html",context)
    
def profiles(request):
    kullanicilar=Profiles.objects.filter(owner=request.user)
    print(kullanicilar)
    context={
        "kullanicilar":kullanicilar
    }
    return render(request,"browse.html",context)

def giris(request):
    return render(request,"login.html")
