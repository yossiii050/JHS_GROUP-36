from django.urls import path
from django.contrib import admin  
from tech import views

urlpatterns = [
    path('ticket/',views.create_ticket,name="ticket"),
    path('tech_tickets/',views.techtickets,name="tech_tickets"),
    path('',views.techhome,name="techhome"),
    #path("",views.tech_main,name="tech-home"),
    path("tech_approve_employer",views.tech_approve_employer, name = "approve" ),
    path("tech_approve_employer",views.update_status, name = "update-status" ),
    path('tickets/<int:ticket_id>/update/', views.update_ticket, name='update_ticket'),
    path('tickets/<int:ticket_id>/closed/', views.close_ticket, name='closed_ticket'),
]

