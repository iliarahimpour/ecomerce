from django.contrib import admin
from .models import Shirt , Jeans ,Shoes , Set , Category , Type

class CatAdmin(admin.ModelAdmin):
    list_display=["cat"]
class ShirtAdmin(admin.ModelAdmin):
    list_display=["title","category"]
class JeanAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]
class SetAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]
class ShoesAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]
    
class TypeAdmin(admin.ModelAdmin):
    list_display=["type","Category"]

admin.site.register(Category,CatAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Set,SetAdmin)
admin.site.register(Shirt , ShirtAdmin)
admin.site.register(Jeans ,JeanAdmin)
admin.site.register(Shoes ,ShoesAdmin)
