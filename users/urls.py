from django.urls import path
from users import views
from django.views.generic import View

urlpatterns = [
    path('employer/', views.employerRegPage,name='employer register'), 
    path('candidate/', views.candidateRegPage,name='candidate register'),
    path('vie/',views.stud,name="stud"),
]
