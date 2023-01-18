from django.test import TestCase , SimpleTestCase
from .models import Shirt  , Jeans , Set , Type , Category , Shoes

# /-----------------------------------------------



# class PageExistTests(TestCase):
#     def test_home_Page(slef):
#         reponse=slef.client.get('/home')
#         slef.assertEqual(reponse.status_code , 200)

#     def test_shirt_Page(slef):
#         reponse=slef.client.get('/product-category/shoes')
#         slef.assertEqual(reponse.status_code , 200)

#     def test_jean_Page(slef):
#         reponse=slef.client.get('/product-category/jeans')
#         slef.assertEqual(reponse.status_code , 200)

#     def test_shirt_Page(slef):
#         reponse=slef.client.get('/product-category/shirts')
#         slef.assertEqual(reponse.status_code , 200)

#     def test_set_Page(slef):
#         reponse=slef.client.get('/product-category/sets')
#         slef.assertEqual(reponse.status_code , 200)
    

class ShoesTest(TestCase):
    def test_type(self):
        shoe=Shoes.objects.get(pk=1)
        self.assertEqual(shoe.type , "کفش ورزشی زنانه")