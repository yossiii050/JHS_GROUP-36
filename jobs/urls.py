from django.urls import path
from . import views
#from jobs import views

urlpatterns = [
    path('upload/',views.uploadJob),
    path('update/',views.upldateJob),
    path('uploadList/',views.Upload_list),
    #path('id/',name='jobIndex'), 
]
