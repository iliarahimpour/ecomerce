from django.db import models

# Create your models here.



class Category(models.Model):
    cat=models.CharField(max_length=45)
    def __str__(self):
        return self.cat 


class Type(models.Model):
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    type=models.CharField(max_length=55)
    def __str__(self):
        return self.type 

class Shirt(models.Model):
    PLY_S=(("1","Single-ply") , ("2","Double-ply"))
    COLOR_N=(("red","Red") , ("green" , "Green") , ("black" ,"Black") , ("specific","Specific"))
    title=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    weave_types=models.CharField(max_length=50 , default="noun")
    ply=models.CharField(max_length=30 , choices=PLY_S , default="Single-ply")
    color=models.CharField(max_length=45 , choices=COLOR_N , default="Specific")
    brand=models.CharField(max_length=45)
    price=models.CharField(max_length=60)
    is_publish=models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Jeans(models.Model):
    COLOR_N=(("red","Red") , ("green" , "Green") , ("black" ,"Black") , ("specific","Specific"))
    title=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    weave_types=models.CharField(max_length=50)
    color=models.CharField(max_length=45 , choices=COLOR_N , default="Specific")
    brand=models.CharField(max_length=45)
    price=models.CharField(max_length=60)
    is_publish=models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Shoes(models.Model):
    COLOR_N=(("red","Red") , ("green" , "Green") , ("black" ,"Black") , ("specific","Specific"))
    title=models.CharField(max_length=50)
    type=models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    weave_types=models.CharField(max_length=50)
    color=models.CharField(max_length=45 , choices=COLOR_N , default="Specific")
    brand=models.CharField(max_length=45)
    price=models.CharField(max_length=60)
    is_publish=models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Set(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=50)
    jeans=models.ForeignKey(Jeans, on_delete=models.CASCADE)
    Shirt=models.ForeignKey(Shirt, on_delete=models.CASCADE)
    shoes=models.ForeignKey(Shoes, on_delete=models.CASCADE)
    def __str__(self):
        return self.title