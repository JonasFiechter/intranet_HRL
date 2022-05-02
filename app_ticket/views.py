from django.shortcuts import render, redirect
from .models import Ticket, Sector, TransportRequest
from .forms import TicketForm, TransportRequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .pdf_generator import pdf_generator


@login_required(redirect_field_name='url_login')
def ticket_center_view_it(request):
    if request.user.groups.filter(name='GROUP-NUIAS').exists():
        return render(request, 'app_ticket/it/ticket_center_it.html', 
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_it_history(request):
    if request.user.groups.filter(name='GROUP-NUIAS').exists():
        return render(request, 'app_ticket/it/ticket_center_it_history.html', 
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_infra(request):
    if request.user.groups.filter(name='GROUP-INFRA').exists():
        return render(request, 'app_ticket/infra/ticket_center_infra.html', 
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_infra_history(request):
    if request.user.groups.filter(name='GROUP-INFRA').exists():
        return render(request, 'app_ticket/infra/ticket_center_infra_history.html', 
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_patrimony(request):
    if request.user.groups.filter(name='GROUP-PATRIMONIO').exists():
        return render(request, 'app_ticket/patrimony/ticket_center_patrimony.html',
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')
        
        
@login_required(redirect_field_name='url_login')
def ticket_center_view_patrimony_history(request):
    if request.user.groups.filter(name='GROUP-PATRIMONIO').exists():
        return render(request, 'app_ticket/patrimony/ticket_center_patrimony_history.html',
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_roomcare(request):
    if request.user.groups.filter(name='GROUP-HOTELARIA').exists():
        return render(request, 'app_ticket/roomcare/ticket_center_roomcare.html',
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_roomcare_history(request):
    if request.user.groups.filter(name='GROUP-HOTELARIA').exists():
        return render(request, 'app_ticket/roomcare/ticket_center_roomcare_history.html',
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_transport(request):
    if request.user.groups.filter(name='GROUP-ENGENHARIA').exists():
        return render(request, 'app_ticket/transport/ticket_center_transport.html',
                                {'tickets': TransportRequest.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_transport_history(request):
    if request.user.groups.filter(name='GROUP-ENGENHARIA').exists():
        return render(request, 'app_ticket/transport/ticket_center_transport_history.html',
                                {'tickets': TransportRequest.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_clinical_engeneering(request):
    if request.user.groups.filter(name='GROUP-TRANSPORTE').exists():
        return render(request, 'app_ticket/clinical_engeneering/ticket_center_clinical_engeneering.html',
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


@login_required(redirect_field_name='url_login')
def ticket_center_view_clinical_engeneering_history(request):
    if request.user.groups.filter(name='GROUP-TRANSPORTE').exists():
        return render(request, 'app_ticket/clinical_engeneering/ticket_center_clinical_engeneering_history.html',
                                {'tickets': Ticket.objects.order_by('-id')})
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


def ticket_view_form_it(request):
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

        return render(request, 'app_ticket/it/ticket_form_it.html', {'is_valid': is_valid})
    except:
        pass
    return render(request, 'app_ticket/it/ticket_form_it.html', {'form': form, 'cat_id': cat_id})


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

        return render(request, 'app_ticket/infra/ticket_form_infra.html', {'is_valid': is_valid})
    except:
        pass
    return render(request, 'app_ticket/infra/ticket_form_infra.html', {'form': form, 'cat_id': cat_id,})


def ticket_view_form_patrimony(request):
    form = TicketForm(request.POST or None)
    
    try:
        print('TEST')
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                                sector_id=request.POST.get('sector'),
                                requester_name=request.POST.get('requester_name'),
                                category='PATRIMONIO')
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')

        return render(request, 'app_ticket/patrimony/ticket_form_patrimony.html', 
        {'is_valid': is_valid})
    except:
        pass
    return render(request, 'app_ticket/patrimony/ticket_form_patrimony.html', 
        {'form': form})


def ticket_view_form_clinical_engeneering(request):
    form = TicketForm(request.POST or None)
    
    try:
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                                sector_id=request.POST.get('sector'),
                                requester_name=request.POST.get('requester_name'),
                                machine_description_id=request.POST.get('machine_description'),
                                serial_number=request.POST.get('serial_number'),
                                category='ENGENHARIA')
        
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')

        return render(request, 'app_ticket/clinical_engeneering/ticket_form_clinical_engeneering.html', 
        {'is_valid': is_valid})
    except:
        pass

    return render(request, 'app_ticket/clinical_engeneering/ticket_form_clinical_engeneering.html', 
        {'form': form})


def ticket_view_form_telephony(request):
    form = TicketForm(request.POST or None)

    try:
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get(' sector'),
                              requester_name=request.POST.get('requester_name'),
                              phone_branch=request.POST.get('phone_branch'),
                              category='INFRA')
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')

        return render(request, 'app_ticket/telephony/ticket_form_telephony.html', 
        {'is_valid': is_valid})
    except:
        pass
    return render(request, 'app_ticket/telephony/ticket_form_telephony.html', 
        {'form': form})


def ticket_view_form_roomcare(request):
    form = TicketForm(request.POST or None)

    try:
        ticket = Ticket.objects.create(description=request.POST.get('description'), 
                              sector_id=request.POST.get('sector'),
                              requester_name=request.POST.get('requester_name'),
                              room_number=request.POST.get('room_number'),
                              category='HOTELARIA')
        id_ = ticket.id
        is_valid = True
        ticket.save()
        messages.success(request, message=f'{id_}')

        return render(request, 'app_ticket/roomcare/ticket_form_roomcare.html', 
        {'is_valid': is_valid})
    except:
        pass
    return render(request, 'app_ticket/roomcare/ticket_form_roomcare.html', 
        {'form': form})


def ticket_view_form_transport(request):
    form = TransportRequestForm(request.POST or None)
    sectors = Sector.objects.all()
    hours = ['0' + str(i) + ':00' for i in range(10)]
    hours += [str(i) + ':00' for i in range(12, 24)]
    types = ['Administrativo', 'Materiais', 'Suporte avançado', 'Suporte básico', 'Outros']

    if request.method != 'POST':
        return render(request, 'app_ticket/transport/ticket_form_transport.html', {
        'sectors': sectors,
        'hours': hours,
        'types': types,
        'form': form,})
        
    else:
        try:
            ticket = TransportRequest.objects.create(
                            description=request.POST.get('description'),
                            requester_name=request.POST.get('requester_name'),
                            sector_id=Sector.objects.get(sector_name=(request.POST.get('sector'))).id,
                            phone_branch=request.POST.get('phone_branch'),
                            destination_address=request.POST.get('destination_address'),
                            local_number=request.POST.get('local_number'),
                            quarter_name=request.POST.get('quarter_name'),
                            city_name=request.POST.get('city'),
                            departure_date=request.POST.get('departure_date'),
                            departure_hour=request.POST.get('departure_hour'),
                            destination_contact=request.POST.get('destination_contact'),
                            contact_phone=request.POST.get('contact_phone'),
                            transport_type=request.POST.get('transport_type'),
                            patient_name=request.POST.get('patient_name'),
                            patient_age=request.POST.get('patient_age'),
                            category='TRANSPORTE'
                            )
            id_ = ticket.id
            is_valid = True
            ticket.save()
            messages.success(request, message=f'{id_}')

            return render(request, 'app_ticket/transport/ticket_form_transport.html', {
                'is_valid': is_valid
            })

        except:
            messages.error(request, message='OCORREU UM ERRO!')
            return render(request, 'app_ticket/transport/ticket_form_transport.html', {
            'sectors': sectors,
            'hours': hours,
            'types': types,
            'form': form,})


def get_group_id(group_name):
    return Group.objects.get(name=group_name).id


def ticket_single_view(request, ticket_id, ticket_type):
    if ticket_type == 'NORMAL':
        ticket = Ticket.objects.get(id=ticket_id)
    elif ticket_type == 'TRANSPORTE':
        ticket = TransportRequest.objects.get(id=ticket_id)
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
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)

        ticket, p, buffer = pdf_generator(ticket, p, buffer)
        return FileResponse(buffer, as_attachment=True, filename=f'ticket_{ticket.id}.pdf')

    return render(request, 'app_ticket/single_ticket.html', {
        'ticket': ticket, 'users':users
    })

