from django.urls import path
from jobs.views import Upload_list
from polls import views
from django.contrib.staticfiles.views import serve
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home page site'),
    path('toggle-maintenance-mode/', views.toggle_maintenance_mode, name='toggle_maintenance_mode'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('jobs/',Upload_list,name='uplodelist'),
    
    #path('', views.home_template, name='home page site'),
]