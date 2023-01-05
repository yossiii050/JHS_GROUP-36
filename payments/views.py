from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

def add_user_to_vip_group(request):
  if request.method == 'POST':
    user= request.user 
    group = Group.objects.get(name='VIP')
    user.groups.add(group)
  return render(request, 'home.html')

def ifEmployer(request):
  for group in request.user.groups.all:
    if group.name == 'Employers':
      return True
  return False    

def paymentpage(request):
    user= request.user 
    group = Group.objects.get(name='VIP')
    user.groups.add(group)
    return render(request,'paymentview.html')

