from django.shortcuts import render
from .models import Shirt , Shoes ,Jeans , Category
from django.utils import timezone
from django.http import HttpResponse , Http404
# Create your views here.


def home(request):
     contex=Shoes.objects.all()[0:3]
     return render(request, "market/homepage.html", {"shoes":contex})


def product(request , pk):
     try :
          pk=Shoes.objects.get(pk=pk)
          return render(request ,"market/product_dedatil.html" ,{"product":pk} )
     except:
          return Http404("The page ,wich you were looking , cannot find!")


def all(request):
     try :
          context=Shoes.objects.all()
          return render(request ,"market/product_dedatil.html" ,{"shoes":context} )
     except:
          return Http404("The page ,wich you were looking , cannot find!")