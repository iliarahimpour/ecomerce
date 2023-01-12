from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('' , views.home , name="home"),
    path('product/<int:pk>/' , views.product , name='product'),
    path('product/shoes/' , views.all , name='all'),
]

urlpatterns += staticfiles_urlpatterns()