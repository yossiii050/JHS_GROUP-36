from django.urls import path

from polls import views

urlpatterns = [
    #path('', views.home_page_view, name='home page site'),
    path('', views.home_template, name='home page site'),
]