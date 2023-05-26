from django.urls import path 
from .views import index, create, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('/criar', create, name='criar'),
    path('/atualizar/<int:user_id>', update, name='atualizar'),
    path('/deletar/<int:user_id>', delete, name='deletar')
]