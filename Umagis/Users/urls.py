from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('info/', views.student1, name='student1'),
    path('madagascar/', views.contry, name='mada'),

]