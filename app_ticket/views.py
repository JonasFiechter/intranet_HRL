from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


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

@login_required(redirect_field_name='url_login')
def ticket_center_view_infra(request):
    if request.user.groups.filter(name='GROUP-INFRA').exists():
        return render(request, 'app_ticket/ticket_center_infra.html', 
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


def get_group_id(group_name):
    return Group.objects.get(name=group_name).id


def ticket_single_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    is_valid = False
    users = User.objects.filter(groups=get_group_id('GROUP-' + ticket.category))

    if request.POST.get('answer-btn'):
        ticket.response_user_id = request.user.id
        ticket.status = 'Atendido'
        ticket.save()
        messages.success(request, message='Chamado atendido!')
        return render(request, 'app_ticket/single_ticket.html', {
            'ticket': ticket, 'users':users
            })

    if request.POST.get('user-input'):
        user_input = request.POST.get('user-input')
        user_id = User.objects.filter(first_name=user_input.split(' ')[0])[0].id
        try:
            ticket.response_user_id = user_id
            ticket.status = 'Finalizado'
            ticket.save()
            messages.success(request, message='Chamado Finalizado!')
            is_valid = True

            return render(request, 'app_ticket/single_ticket.html', {
                'ticket': ticket, 'is_valid':is_valid
                })
        except:
            pass

    return render(request, 'app_ticket/single_ticket.html', {
        'ticket': ticket, 'users':users
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


def ticket_view_form_infra(request):
    form = TicketForm(request.POST or None)
    cat_id = 0
    
    try:
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get('sector'),
                              requester_name=request.POST.get('requester_name'),
                              category='INFRA')
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')

        return render(request, 'app_ticket/ticket_form_infra.html', {'is_valid': is_valid})
    except:
        pass
    return render(request, 'app_ticket/ticket_form_infra.html', {'form': form, 'cat_id': cat_id,})
