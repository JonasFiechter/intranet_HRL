from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib import messages
from django.db.models.functions import Cast

# Create your views here.

def ticket_view_nuias(request):
    data = {'tickets': Ticket.objects.all()}
    return render(request, 'app_ticket/ticket.html', data)


def ticket_view_nuias_form(request):
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
        messages.success(request, message=f'Chamado enviado com sucesso! '
                                          f'Anote o número do chamado: {id_}')
        form.clean()

        return render(request, 'app_ticket/ticket_nuias_form.html', {'form': form, 'is_valid': is_valid})
    return render(request, 'app_ticket/ticket_nuias_form.html', {'form': form})


def ticket_view_infra_form(request):
    form = TicketForm(request.POST or None)

    if form.is_valid():
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get('sector'), 
                              machine_number=request.POST.get('machine_number'), 
                              requester_name=request.POST.get('requester_name'), 
                              category='Infraestrutura')
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'Chamado enviado com sucesso! '
                                          f'Anote o número do chamado: {id_}')
        form.clean()
        
        return render(request, 'app_ticket/ticket_infra_form.html', {'form': form, 'is_valid': is_valid})
    return render(request, 'app_ticket/ticket_infra_form.html',  {'form': form})