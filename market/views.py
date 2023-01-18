from django.shortcuts import render
from .models import Shoes
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
# ---------------------------------------------

# Class-Based Views /////////////////////////

class ShoesPageView(TemplateView):
   template_name = 'market/shoespage.html'
 

# ////////////////////////////////////////////

# Function-Based Views /////////////////////////
def home(request):
    shoes = Shoes.objects.all()
    return render(request, "market/homepage.html", {"shoes": shoes})


def product_detail(request, pk):
    try:
        pk = Shoes.objects.get(pk=pk)
        return render(request, "market/product_dedatil.html", {"product": pk})
    except:
        return Http404("The page ,wich you were looking , cannot find!")


# def all_shirta(request):
#     try:
#         context = Shirt.objects.all()
#         return render(request, "market/product_dedatil.html", {"shirts": context})
#     except:
#         return Http404("The page ,wich you were looking , cannot find!")

def deafult(request):
    return HttpResponse("Dear MAN")

# ////////////////////////////////////////////