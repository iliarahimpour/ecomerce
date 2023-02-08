from django.shortcuts import render
from .models import Shoes , Type , Category ,Brand ,Image
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
  
        shoes = Shoes.objects.all()[:3]
        nike_shoes=Shoes.objects.filter(Witch_brnad=3).order_by("-publish_date")[:3]
        converse_shoes=Shoes.objects.filter(Witch_brnad=5).order_by("-publish_date")[:3]
        adidas_shoes=Shoes.objects.filter(Witch_brnad=8).order_by("-publish_date")[:3]
        # converse_shoes=Shoes.objects.filter(brand="Converse")[:3]
        # skechers_shoes=Shoes.objects.filter(brand="SKECHERS")[:3]
        return render(request, "market/homepage.html",{"Shoes":shoes ,"Nikes":nike_shoes, "Converse": converse_shoes , "Adidas":adidas_shoes})


def product_women(request,cat):
    try:
        cat=Type.objects.get(type=cat)
        context=Shoes.objects.filter(type=cat)
        return render(request,"market/Women_Product_list_page.html" , {"shoes":context , "cat":cat})
    except:
        return render(request,"market/404-error.html",{})

def product_men(request,cat):
    try:
        cat=Type.objects.get(type=cat)
        context=Shoes.objects.filter(type=cat)
        return render(request,"market/Men_Product_list_page.html" , {"shoes":context , "cat":cat})
    except:
        return render(request,"market/404-error.html",{})


def error(request):
    return render(request,"market/404-error.html",{})

def imagetes(request):
      images=Image.objects.all()
      return render(request,"market/qhello.html",{"image":images})

def categoryShoe(request , category):
    try:
        cat=Category.objects.get(cat=category)
        context=Shoes.objects.filter(category=cat)
        return render(request,"market/orderd_categoru_shoes.html",{"Shoes":context})
    except:
        return render(request,"market/404-error.html",{})

def brand_type_op(request , brand):
    # try:
        type_brand=Brand.objects.get(brand=brand)
        context=Shoes.objects.filter(Witch_brnad=type_brand)
        return render(request,"market/orderd_brand_shoes.html",{"Shoes":context,"Brand":type_brand})
    # except:
    #      return render(request,"market/404-error.html",{})

# def brand_type_op(request,brand):
#     try:
#         context=Shoes.objects.filter(brand=brand)
#         return render(request, "market/Hello.html",{"Shoes":context})
#     except:
#          return render(request,"market/404-error.html",{})


# def product_detail(request, pk):
#     try:
#         pk = Shoes.objects.get(pk=pk)
#         return render(request, "market/product_dedatil.html", {"product": pk})
#     except:
#         return Http404("The page ,wich you were looking , cannot find!")


# def deafult(request):
#     return HttpResponse("Dear MAN")

# ////////////////////////////////////////////