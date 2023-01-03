from django.shortcuts import render

from django.contrib.auth.models import User, Group

def add_user_to_vip_group(request):
  if request.method == 'POST':
    email = request.POST['email']
    user = User.objects.get(email=email)
    vip_group = Group.objects.get(name='VIP')
    vip_group.user_set.add(user)
  return render(request, 'home.html')


def paymentpage(request):
    return render(request,'paymentview.html')

