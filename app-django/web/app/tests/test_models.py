from django.test import TestCase 

from app.models import User 


class StrTest(TestCase):
    # função que executada primeiro
    def setUp(self):
        self.user = User(nome="Valdir",telefone=11977601187,email="valdirpiresba@hotmail.com")

    def test_str(self):
        self.assertEquals(str(self.user),"Nome: Valdir, Telefone: 11977601187, Email: valdirpiresba@hotmail.com ")  


