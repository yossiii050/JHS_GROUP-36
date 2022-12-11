from django.urls import path
from users import views

urlpatterns = [
    path('employer/', views.employerRegPage,name='employer register'), 
    path('candidate/', views.candidateRegPage,name='candidate register'),
]
