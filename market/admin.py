from django.contrib import admin
from .models import Shoes  , Category , Type ,Image ,Brand

class CatAdmin(admin.ModelAdmin):
    list_display=["cat"]

class ShoesAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]
    
class TypeAdmin(admin.ModelAdmin):
    list_display=["type","Category"]
    
class ImageAdmin(admin.ModelAdmin):
    list_display=["shoe"]
class BrandAdmin(admin.ModelAdmin):
    list_display=["brand"]

admin.site.register(Category,CatAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Shoes ,ShoesAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Brand,BrandAdmin)
