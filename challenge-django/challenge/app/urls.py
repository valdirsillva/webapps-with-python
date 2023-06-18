from django.urls import path 
# from .views import index
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('/calculate', views.calculate, name='calculate'),
]