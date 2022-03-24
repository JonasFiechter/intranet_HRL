from textwrap import fill
from turtle import fillcolor
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


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


@login_required(redirect_field_name='url_login')
def ticket_center_view_infra_history(request):
    if request.user.groups.filter(name='GROUP-INFRA').exists():
        return render(request, 'app_ticket/ticket_center_infra_history.html', 
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
        ticket.response_user = str(request.user)
        ticket.status = 'Atendido'
        ticket.save()
        messages.success(request, message='Chamado atendido!')
        return render(request, 'app_ticket/single_ticket.html', {
            'ticket': ticket, 'users':users
            })

    if request.POST.get('user-input'):
        user_input = request.POST.get('user-input')
        # user_response_id = User.objects.filter(first_name=user_input.split(' ')[0])[0].id
        try:
            ticket.response_user = user_input
            ticket.status = 'Finalizado'
            ticket.save()
            messages.success(request, message='Chamado Finalizado!')
            is_valid = True

            return render(request, 'app_ticket/single_ticket.html', {
                'ticket': ticket, 'is_valid':is_valid
                })
        except:
            pass
    
    if request.POST.get('print-btn'):
        print('BTN WORKS')
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.setFontSize(size=12)
        p.drawString(230, 800, f'Hospital Regional do Litoral')
        p.setFontSize(size=10)
        p.drawString(250, 780, f'Chamado Técnico n°: {ticket.id}')
        p.setFontSize(size=9)
        p.drawString(50, 700, f"Responsável Técnico: {ticket.response_user}")
        p.rect(50, 50, 480, 100, stroke=1, fill=0)
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f'ticket_{ticket.id}.pdf')

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
