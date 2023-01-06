from django.urls import path
from users import views
from django.views.generic import View


urlpatterns = [
    path('employer/', views.employerRegPage,name='employer register'), 
    path('candidate/', views.candidateRegPage,name='candidate register'),
    path('cv/', views.cv,name="cv"),  
    path('',views.usershome,name="home"),
    path('Profile/<username>',views.view_profile,name="Profile"),
]
