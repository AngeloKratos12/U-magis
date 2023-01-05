from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.forum_home, name='forumhome'),
    path("showtopic/", views.showtopic, name="showtopic"),
    path('addtopic/', views.addtopic, name='addtopic'),
    #path('addanswer/', views.addanswer, name='addanswer'),

]