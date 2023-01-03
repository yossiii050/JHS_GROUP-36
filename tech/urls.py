from django.urls import path
from django.contrib import admin  
from tech import views

urlpatterns = [
    path('ticket/',views.create_ticket,name="ticket"),
    path('',views.techhome,name="home"),
    
]
