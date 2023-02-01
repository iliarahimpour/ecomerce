from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ShoesPageView ,WomenProductView , MenProductView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# --------------------------------------------------

urlpatterns = [
    path('', views.home, name="home"),
    path('Kids', ShoesPageView.as_view(), name='ShoesPageView'),
    path('womens',WomenProductView.as_view() ,name='WomenProductView'),
    path('mens',MenProductView.as_view() ,name='MenProductView'),
    path("womens/<str:cat>", views.product_women, name="product_women"),
    path("men/<str:cat>", views.product_men, name="product_men"),
    path("error", views.error, name="error"),
    # path("brand_type/<str:brand>", views.brand_type_op, name="brand_type"),
    # path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()