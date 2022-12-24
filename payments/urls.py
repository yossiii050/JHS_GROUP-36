from django.urls import path
from payments.views import paymentpage

urlpatterns = [
    path('', paymentpage, name='paymentpage'),
    
]