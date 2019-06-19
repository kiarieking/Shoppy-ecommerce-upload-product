from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
        path('index/', IndexView, name='index'),
        path('add_product/', AddProductView, name='add_product')
    ]

