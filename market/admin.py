from django.contrib import admin
from .models import Shoes  , Category , Type

class CatAdmin(admin.ModelAdmin):
    list_display=["cat"]

class ShoesAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]
    
class TypeAdmin(admin.ModelAdmin):
    list_display=["type","Category"]

admin.site.register(Category,CatAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Shoes ,ShoesAdmin)
