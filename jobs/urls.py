from django.urls import path
from . import views
from .views import job_details
#from jobs import views

urlpatterns = [
    path('upload/',views.uploadJob,name='upload'),
    path('update/<str:upload_id>',views.updateJob,name='update'),
    path('',views.Upload_list,name='list'),
    path('<str:slug>',views.job_details,name='job_details'),
    path('success/',views.success,name='success'),
    path('deleteJob/<str:upload_id>',views.deleteJob,name='deleteJob'),
    path('ApllyCv/<str:upload_id>',views.applyCv,name='ApllyCv'),
    path('jobsCsvFile/',views.jobscsvFile,name='jobscsvFile'),
    path('jobsLocationPdfFile/',views.jobsLocationPdfFile,name='jobsLocationPdfFile'),
    path('jobsPriorityPdfFile/',views.jobsPriorityPdfFile,name='jobsPriorityPdfFile'),
    path('update_user/<str:username>', views.update_user, name='update_user'),
    path('abort_user/<str:username>', views.abort_user, name='abort_user'),
    path('hired/<str:username>',views.hired_user,name='hired_user'),
]

