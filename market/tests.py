from django.test import TestCase , SimpleTestCase
# /-----------------------------------------------



class SimpleTest(TestCase):
    def test_home_Page(slef):
        reponse=slef.client.get('/home')
        slef.assertEqual(reponse.status_code , 200)

    def test_shirt_Page(slef):
        reponse=slef.client.get('/product-category/shoes')
        slef.assertEqual(reponse.status_code , 200)

    def test_jean_Page(slef):
        reponse=slef.client.get('/product-category/jeans')
        slef.assertEqual(reponse.status_code , 200)

    def test_shirt_Page(slef):
        reponse=slef.client.get('/product-category/shirts')
        slef.assertEqual(reponse.status_code , 200)

    def test_set_Page(slef):
        reponse=slef.client.get('/product-category/sets')
        slef.assertEqual(reponse.status_code , 200)
    