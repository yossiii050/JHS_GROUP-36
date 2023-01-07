from django.urls import path
from payments.views import paymentpage,add_user_to_vip_group

urlpatterns = [
    path('', paymentpage, name='paymentpage'),
    path('add_user_to_vip_group/', add_user_to_vip_group, name='add_user_to_vip_group'),

]