from unicodedata import category
from django.shortcuts import render, redirect
from .models import Ticket, Category
from .forms import TicketForm
from django.contrib import messages
from django.db.models.functions import Cast

# Create your views here.

def ticket_center_view_nuias(request):
    return render(request, 'app_ticket/ticket_center_nuias.html', 
                            {'tickets': Ticket.objects.filter(category_id=2)})


def ticket_view_form(request):
    form = TicketForm(request.POST or None)
    stage = 1
    cat_id = 0
    
    try:
        cat_id = form.data['category']
        stage = 2
    except:
        pass

    if stage == 2 and len(request.POST.get('description')) > 10:
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get('sector'), 
                              machine_number=request.POST.get('machine_number'), 
                              requester_name=request.POST.get('requester_name'),
                              category=Category.objects.get(id=cat_id))
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')

        return render(request, 'app_ticket/ticket_form.html', {'is_valid': is_valid})
    return render(request, 'app_ticket/ticket_form.html', {'form': form, 'stage': stage, 'cat_id': cat_id})