from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ShoesPageView 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# --------------------------------------------------

urlpatterns = [
    path('', views.home, name="home"),
    path('product-category/shoes', ShoesPageView.as_view(), name='ShoesPageView'),
    path('product-category/shoes/Sneakers', views.deafult, name='deafult'),
    
    # path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += staticfiles_urlpatterns()