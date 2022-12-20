from django.urls import path
from . import views
from .views import job_details
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from jobs import views

urlpatterns = [
    path('upload/',views.uploadJob,name='upload'),
    path('update/',views.updateJob),
    path('',views.Upload_list,name='list'),
    path('<str:slug>',views.job_details,name='detail'),
]

