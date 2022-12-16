from django.urls import path
from django.contrib import admin  
from tech import views

urlpatterns = [
    path('ticket/',views.ticket),
   # path('index/', views.index),  
   path("",views.tech_main),
   path("tech_approve_employer",views.tech_approve_employer, name = "approve" ),
]
