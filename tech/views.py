
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Ticket
from django.core.files import File
from .forms import TicketForm
from django.contrib import messages
from django.template import loader
from django.contrib.auth.models import Group
from django.http import FileResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
                new_ticket = Ticket(
                title=form.cleaned_data['title'],body=form.cleaned_data['body'],user=request.user,handler=request.user,closed_by = request.user)
                new_ticket.save()
                messages.success(request, 'Ticket saved successfully!')
                return render(request, 'ticket.html', {'form': form, 'date':new_ticket.date})
        else:
            messages.success(request, 'Errors,please try again!')   
            return render(request, 'ticket.html', {'form': form})
    else:
        form = TicketForm()
    return render(request, 'ticket.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def techtickets(request):
    # Get the list of tickets from the database
    tickets = Ticket.objects.all()

    users = User.objects.all()
    # Render the template with the tickets and handlers lists
    return render(request, 'tech_tickets.html', {'tickets': tickets, 'users': users})


@user_passes_test(lambda u: u.is_staff)
def techhome(request):
    closed_tickets = Ticket.objects.filter(handler=request.user, isopen=False).count()
    total_tickets = Ticket.objects.all().count()
    closed_tickets=int(closed_tickets)
    total_tickets=int(total_tickets)
    return render(request, 'tech.html', {
    'closed_tickets': closed_tickets,
    'total_tickets': total_tickets,
  })

from sqlite3 import SQLITE_READ

def tech_main (request):
  return render(request,'tech_main.html')


@user_passes_test(lambda u: u.is_staff)
def update_ticket(request, ticket_id):
    # Get the ticket object
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    # Update the handler for the ticket
    if request.method == 'POST':
        handler_id = request.POST['handler']
        handler = User.objects.get(id=handler_id)
        ticket.handler = handler
        ticket.save()
        return redirect('tech_tickets')

    return redirect('tech_tickets')

@user_passes_test(lambda u: u.is_staff)
def close_ticket(request, ticket_id):
    # Get the ticket object
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if request.method == 'POST':
        # Retrieve the reply value from the request.POST dictionary
        new_reply_value = request.POST['reply']

        # Update the Reply field of the ticket object
        ticket.Reply = new_reply_value

        # Update the closed_by field and set isopen to False
        user = get_user_model()
        closed_by = request.user
        ticket.closed_by = closed_by
        ticket.isopen = False
        ticket.save()
        return redirect('tech_tickets')

    return redirect('tech_tickets')




def tech_approve_employer(request):
  form=User.objects.filter(is_active=False)
  #form=Group.name()
  context={'form':form}
  return render(request,'tech_approve_employer.html',context)

def update_status(request):
    if request.method == 'POST':
        User.objects.filter(is_active=False).update(is_active=True)
    return render(request,'tech.html')


def allreports(request):
    alluserform=User.objects.all()
    tickets=Ticket.objects.all()
    vipuser = get_user_model()
    vip_group = Group.objects.get(name='VIP')
    VIPform = vipuser.objects.filter(groups=vip_group)
    Approveform=User.objects.filter(is_active=False)
    context={'alluserform':alluserform,'VIPform':VIPform,'Approveform':Approveform,'tickets':tickets}
    return render(request,'Allreports.html',context)
