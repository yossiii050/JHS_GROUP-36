from django.urls import path

from tech import views

urlpatterns = [
    path('ticket/',views.ticket),
]
