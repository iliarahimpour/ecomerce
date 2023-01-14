from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/shoes/', views.all, name='all'),
]

urlpatterns += staticfiles_urlpatterns()
