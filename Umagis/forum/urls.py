from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.forum_home, name='student'),
    #path('me/', views.portfolio, name='student1'),

]