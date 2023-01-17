from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ShoesPageView , JeansPageView , ShirtPageView , SetsPageView


# --------------------------------------------------

urlpatterns = [
    path('home', views.home, name="home"),
    path('product-category/shoes', ShoesPageView.as_view(), name='ShoesPageView'),
    path('product-category/jeans', JeansPageView.as_view(), name='JeansPageView'),
    path('product-category/shirts', ShirtPageView.as_view(), name='ShirtPageView'),
    path('product-category/sets', SetsPageView.as_view(), name='SetsPageView'),
    
    # path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
