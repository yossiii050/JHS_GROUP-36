from django.urls import path
from . import views
from .views import job_details
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from jobs import views

urlpatterns = [
    path('upload/',views.uploadJob,name='upload'),
    path('update/<str:upload_id>',views.updateJob,name='update'),
    path('',views.Upload_list,name='list'),
    path('<str:slug>',views.job_details,name='detail'),
    path('success/',views.success,name='success'),
    path('deleteJob/<str:upload_id>',views.deleteJob,name='deleteJob'),
    path('jobsCsvFile/',views.jobscsvFile,name='jobscsvFile'),
    path('jobsPdfFile/',views.jobsPdfFile,name='jobsPdfFile')

]

