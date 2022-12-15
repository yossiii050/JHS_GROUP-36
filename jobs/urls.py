from django.urls import path
from . import views
from .views import job_details
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from jobs import views

urlpatterns = [
    path('upload/',views.uploadJob),
    path('update/',views.upldateJob),
    path('',views.Upload_list,name='list'),
    path('<str:pk>',views.job_details,name='detail'),
    #path('job/<int:pk>',job_details,name='job'),
    #path('id/',name='jobIndex'), 
    #path(r'^(?P<abc>[\w-]+/$')
]

#urlpatterns += staticfiles_urlpatterns()
