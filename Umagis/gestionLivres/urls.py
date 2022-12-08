from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.biblio, name='books'),
    path('reservation/', views.makereservation, name='reservatioon'),
    path('borrow/', views.borrow, name='borrow'),

]