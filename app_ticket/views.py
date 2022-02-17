from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib import messages
from django.db.models.functions import Cast

# Create your views here.

def ticket_center_view_nuias(request):
    return render(request, 'app_ticket/ticket_center_nuias.html', {'tickets': Ticket.objects.all()})


def ticket_view_form(request):
    form = TicketForm(request.POST or None)

    if form.is_valid():
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get('sector'), 
                              machine_number=request.POST.get('machine_number'), 
                              requester_name=request.POST.get('requester_name'), 
                              category='Nuias')
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')
        form.clean()

        return render(request, 'app_ticket/ticket_form.html', {'form': form, 'is_valid': is_valid})
    return render(request, 'app_ticket/ticket_form.html', {'form': form})