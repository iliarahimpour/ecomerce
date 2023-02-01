from django.db import models
from django.utils import timezone

class Category(models.Model):
    cat = models.CharField(max_length=45)
    def __str__(self):
        return self.cat

class Type(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=55)
    title = models.CharField(max_length=50, blank=True, default="default")
    def __str__(self):
        return self.type
    
class Brand(models.Model):
    brand=models.CharField(max_length=50)
    def __str__(self):
        return self.brand


class Shoes(models.Model):
    COLOR_N = (("red", "Red"), ("green", "Green"),
               ("black", "Black"), ("specific", "Specific"))
    GENDER = (("woman", "Woman"), ("man", "Man"),
               ("kid", "Kid"))
    gender=models.CharField(max_length=50, choices=GENDER, default="Specific")
    title = models.CharField(max_length=50)
    Witch_brnad=models.ForeignKey(Brand, on_delete=models.DO_NOTHING ,default="brand")
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weave_types = models.CharField(max_length=50)
    color = models.CharField(
        max_length=45, choices=COLOR_N, default="Specific")
    publish_date=models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=60)
    is_publish = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    
class Image(models.Model):
        shoe=models.ForeignKey(Shoes,on_delete=models.CASCADE)
        title=models.CharField(max_length=50 ,blank=True,default="Noun")
        Product_main_image = models.ImageField(
        upload_to='media', blank=True, default="hello", )
        def __str__(self):
            return self.title