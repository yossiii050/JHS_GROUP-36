from django.urls import path

from polls import views

urlpatterns = [
    path('', views.home_template, name='home page site'),
    path('toggle-maintenance-mode/', views.toggle_maintenance_mode, name='toggle_maintenance_mode'),
    path('maintenance/', views.maintenance, name='maintenance'),

    #path('', views.home_template, name='home page site'),
]