from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.biblio, name='books'),
    path('borrow/', views.borrow, name='borrow'),

]