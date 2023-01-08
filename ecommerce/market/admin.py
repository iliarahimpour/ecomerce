from django.contrib import admin
from .models import Shirt , Jeans ,Shoes , Set , Category

class CatAdmin(admin.ModelAdmin):
    list_display=["cat","type"]
class ShirtAdmin(admin.ModelAdmin):
    list_display=["title","category"]
class JeanAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]
class SetAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]
class ShoesAdmin(admin.ModelAdmin):
    list_display=["title","category","type"]

admin.site.register(Category,CatAdmin)
admin.site.register(Set,SetAdmin)
admin.site.register(Shirt , ShirtAdmin)
admin.site.register(Jeans ,JeanAdmin)
admin.site.register(Shoes ,ShoesAdmin)
