from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from jobs import views

urlpatterns = [
    path('upload/',views.uploadJob),
    path('update/',views.upldateJob),
    path('uploadJobsList/',views.Upload_list),
    #path('id/',name='jobIndex'), 
]

urlpatterns += staticfiles_urlpatterns()
