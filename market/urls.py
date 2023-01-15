from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name="home"),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/shoes/', views.all, name='all'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
