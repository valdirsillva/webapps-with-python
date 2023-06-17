from django.test import TestCase 
from django.test import Client
from django.urls import reverse_lazy 
from app.models import User


class ViewTest(TestCase):
    def setUp(self):
        self.data = {
            'nome': 'Jhon Jhoe',
            'telefone': 2199887557,
            'email': 'jhondoe@email.com.br'
        }

        self.client = Client()

    def test_index(self):
        request = self.client.get(reverse_lazy('index'))
        self.assertEquals(request.status_code, 200)

    def test_criar(self):
        request = self.client.post(reverse_lazy('criar'), data=self.data)
        self.assertEquals(request.status_code, 302) 
        
