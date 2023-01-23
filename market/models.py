from django.db import models


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


class Shoes(models.Model):
    COLOR_N = (("red", "Red"), ("green", "Green"),
               ("black", "Black"), ("specific", "Specific"))
    title = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weave_types = models.CharField(max_length=50)
    color = models.CharField(
        max_length=45, choices=COLOR_N, default="Specific")
    brand = models.CharField(max_length=45)
    price = models.CharField(max_length=60)
    is_publish = models.BooleanField(default=False)
    hotel_Main_Img = models.ImageField(
        upload_to='media', blank=True, default="hello", )

    def __str__(self):
        return self.title
