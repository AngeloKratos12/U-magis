from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('reservation/', views.makereservation, name='reservatioon'),
    path('emprunte/', views.borrow, name='borrow'),

]