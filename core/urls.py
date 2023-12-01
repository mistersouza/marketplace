from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('contact/', views.contact, name='contact'),
]