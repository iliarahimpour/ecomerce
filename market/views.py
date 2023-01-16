from django.shortcuts import render
from .models import Shirt, Shoes, Jeans, Category
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
# ---------------------------------------------

# Class-Based Views /////////////////////////

class ShoesPageView(TemplateView):
   template_name = 'market/shoespage.html'
 

class JeansPageView(TemplateView):
    template_name = 'market/jeanpage.html'


class ShirtPageView(TemplateView):
    template_name = 'market/shirstpage.html'


class SetsPageView(TemplateView):
    template_name = 'market/setspage.html'
# ////////////////////////////////////////////

# Function-Based Views /////////////////////////
def home(request):
    shoes = Shoes.objects.all()[0:3]
    shirts = Shirt.objects.all()
    Jeans = Shirt.objects.all()
    return render(request, "market/homepage.html", {"shoes": shoes, "shirts": shirts, "jeans": Jeans})


def product_detail(request, pk):
    try:
        pk = Shoes.objects.get(pk=pk)
        return render(request, "market/product_dedatil.html", {"product": pk})
    except:
        return Http404("The page ,wich you were looking , cannot find!")


def all_shirta(request):
    try:
        context = Shirt.objects.all()
        return render(request, "market/product_dedatil.html", {"shirts": context})
    except:
        return Http404("The page ,wich you were looking , cannot find!")
# ////////////////////////////////////////////