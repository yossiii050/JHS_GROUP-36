from django.urls import path
from django.contrib import admin  
from tech import views

urlpatterns = [
    path('ticket/',views.ticket),
   # path('index/', views.index),  
]
