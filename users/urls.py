from django.urls import path
from users import views
from django.views.generic import View


urlpatterns = [
    path('employer/', views.employerRegPage,name='employer register'), 
    path('candidate/', views.candidateRegPage,name='candidate register'),
    path('cv/', views.cv,name="cv"),  
    path('',views.usershome,name="home"),
    path('Profile/<str:username>/',views.user_profile,name="Profile"),
    path('Profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('Profile/<str:username>/jobslist',views.jobsList,name='jobs_list')
    ]
