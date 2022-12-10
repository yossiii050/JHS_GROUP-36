from django.urls import path

from users import views

urlpatterns = [
    path('employer/', views.reg,name='employer register'), 
    path('candidate/', views.reg,name='candidate register'),
]
