from django.urls import path

from tech import views

urlpatterns = [
    path('reg22/', views.reg22,name='tech job'),
    path('ticket/',views.ticket,name='ticket'),
]
