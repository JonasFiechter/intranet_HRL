from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib import messages

# Create your views here.

def ticket_center_view_ti(request):
    return render(request, 'app_ticket/ticket_center_ti.html', 
                            {'tickets': Ticket.objects.all()})


def ticket_center_view_infraestrutura(request):
    return render(request, 'app_ticket/ticket_center_infraestructura.html', 
                            {'tickets': Ticket.objects.all()})


def ticket_view_form_ti(request):
    form = TicketForm(request.POST or None)
    cat_id = 0
    
    try:
        cat_id = form.data['category']
        print(f'this is cat_id: {cat_id}')
    except:
        pass

    try:
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get('sector'), 
                              machine_number=request.POST.get('machine_number'), 
                              requester_name=request.POST.get('requester_name'),
                              category='NUIAS')
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')

        return render(request, 'app_ticket/ticket_form_ti.html', {'is_valid': is_valid})
    except:
        pass
    return render(request, 'app_ticket/ticket_form_ti.html', {'form': form, 'cat_id': cat_id,})

def ticket_view_form_infraestrutura(request):
    form = TicketForm(request.POST or None)

    if form.is_valid():
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get('sector'), 
                              machine_number=request.POST.get('machine_number'), 
                              requester_name=request.POST.get('requester_name'),
                              category='Infraestrutura')