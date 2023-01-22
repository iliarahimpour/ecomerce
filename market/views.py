from django.shortcuts import render
from .models import Shoes , Type , Category
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView , ListView
# ---------------------------------------------

# Class-Based Views /////////////////////////
class ShoesPageView(TemplateView):
   template_name = 'market/shoespage.html'


class WomenProductView(ListView):
    model=Shoes
    template_name='market/womenpage.html'
class MenProductView(ListView):
    model=Shoes
    template_name='market/menspage.html'
# ////////////////////////////////////////////


# Function-Based Views /////////////////////////
def home(request):
    shoes = Shoes.objects.all()
    nike_shoes=Shoes.objects.filter(brand="Nike")[:3]
    converse_shoes=Shoes.objects.filter(brand="Converse")
    skechers_shoes=Shoes.objects.filter(brand="SKECHERS")
    return render(request, "market/homepage.html",{"shoes":shoes ,"nike_shoes":nike_shoes , "converse_shoes":converse_shoes,"skechers_shoes":skechers_shoes})


def product(request,cat):
    cat=Type.objects.get(type=cat)
    context=Shoes.objects.filter(type=cat)
    return render(request,"market/WomenBoot.html" , {"shoes":context , "cat":cat})


# def product_detail(request, pk):
#     try:
#         pk = Shoes.objects.get(pk=pk)
#         return render(request, "market/product_dedatil.html", {"product": pk})
#     except:
#         return Http404("The page ,wich you were looking , cannot find!")


# def deafult(request):
#     return HttpResponse("Dear MAN")

# ////////////////////////////////////////////