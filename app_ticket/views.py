from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='url_login')
def ticket_center_view_ti(request):
    if request.user.groups.filter(name='GROUP-NUIAS').exists():
        return render(request, 'app_ticket/ticket_center_ti.html', 
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_ti_history(request):
    if request.user.groups.filter(name='GROUP-NUIAS').exists():
        return render(request, 'app_ticket/ticket_center_ti_history.html', 
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


def ticket_center_view_infraestrutura(request):
    return render(request, 'app_ticket/ticket_center_infraestructura.html', 
                                {'tickets': Ticket.objects.all()})


def ticket_single_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = TicketForm(request.POST or None)
    is_valid = False

    if request.POST.get('response_user'):
        try:
            ticket.response_user_id = request.POST.get('response_user')
            ticket.status = 'Atendido'
            ticket.save()
            messages.success(request, message='Chamado atendido com sucesso!')
            is_valid = True

            if ticket.category == 'NUIAS':
                return render(request, 'app_ticket/single_ticket.html', {
                    'ticket': ticket, 'form': form, 'is_valid':is_valid
                })
        except:
            pass

    return render(request, 'app_ticket/single_ticket.html', {
        'ticket': ticket, 'form': form
    })


def ticket_view_form_ti(request):
    form = TicketForm(request.POST or None)
    cat_id = 0
    
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