from datetime import datetime
from email import message
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Ticket, Sector, TransportRequest
from .forms import TicketForm, TransportRequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from locale import setlocale, LC_ALL
from datetime import datetime


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

        min_x = 0
        min_y = 0
        max_x = 595
        max_y = 842

        p.setFontSize(size=12)
        p.setFont('Helvetica-Bold', 12)
        p.drawCentredString(max_x/2, 760, f'Hospital Regional do Litoral')
        p.drawCentredString(x=max_x/2, y=740, text=f'Chamado Técnico n°: {ticket.id}')

        setlocale(LC_ALL, 'pt_BR.utf-8')
        p.setFont('Helvetica', 10)

        p.drawString(50, 700, f"Nº do chamado:")
        p.drawString(160, 700, f"{ticket.id}")

        p.drawString(50, 685, f"Data da requisição:")
        p.drawString(160, 685, f"{ticket.date.strftime('%A, %d, de %B de %Y | %H:%M:%S')}")

        p.drawString(50, 670, f"Responsável técnico:")
        p.drawString(160, 670, f"{ticket.response_user.upper()}")

        p.drawString(50, 655, f"Solicitante:")
        p.drawString(160, 655, f"{ticket.requester_name.upper()}")

        p.rect(45, 650, max_x-90, 62, stroke=1, fill=0)
        p.line(155, 650, 155, 712)

        p.line(45, 666, max_x-45, 666)
        p.line(45, 681, max_x-45, 681)
        p.line(45, 696, max_x-45, 696)

        p.drawString(x=min_x+50, y=620, text="Descrição do problema:")
        p.rect(min_x+45, 427, max_x-90, 204, stroke=1, fill=0)
        p.line(x1=min_x+45, y1=616, x2=max_x-45, y2=616)

        ticket_description = f'{ticket.description}'
        c = 0
        for n, letter in enumerate(ticket_description):
            if letter == ' ':
                c += 1
                if c == 17 or c == 34 or c == 54 or c == 68:
                    print(n)
                    t_list = list(ticket_description)
                    ticket_description = ''
                    t_list[n] = '\n'
                    for l in t_list:
                        ticket_description += l

        description_text = p.beginText(x=min_x+50, y=605)

        for line in ticket_description.splitlines(True):
            description_text.textLine(line.rstrip())
        p.drawText(description_text)

        p.drawString(x=min_x+50, y=496, text='Observações:')
        p.line(x1=min_x+45, y1=488, x2=max_x-45, y2=488)
        p.line(x1=min_x+45, y1=476, x2=max_x-45, y2=476)
        p.line(x1=min_x+45, y1=464, x2=max_x-45, y2=464)
        p.line(x1=min_x+45, y1=452, x2=max_x-45, y2=452)
        p.line(x1=min_x+45, y1=440, x2=max_x-45, y2=440)

        p.drawString(x=min_x+50, y=388, text="Situação:")
        p.rect(min_x+45, 320, max_x-90, 80, stroke=1, fill=0)
        p.line(x1=min_x+45, y1=385, x2=max_x-45, y2=386)
        p.rect(65, 344, 20, 20, stroke=1, fill=0)
        p.drawString(x=93, y=350, text="Resolvido")
        p.rect(300, 344, 20, 20, stroke=1, fill=0)
        p.drawString(x=325, y=350, text="Não resolvido")

        p.rect(min_x+45, 200, max_x-90, 90, stroke=1, fill=0)
        p.drawString(x=50, y=278, text="Descritivo técnico:")
        p.line(x1=min_x+45, y1=260, x2=max_x-45, y2=260)
        p.line(x1=min_x+45, y1=248, x2=max_x-45, y2=248)
        p.line(x1=min_x+45, y1=236, x2=max_x-45, y2=236)
        p.line(x1=min_x+45, y1=224, x2=max_x-45, y2=224)
        p.line(x1=min_x+45, y1=212, x2=max_x-45, y2=212)
        
        p.line(x1=min_x+80, y1=90, x2=min_x+250, y2=min_x+90)
        p.line(x1=min_x+350, y1=90, x2=max_x-80, y2=min_x+90)
        p.drawCentredString(x=min_x+160, y=78, text=f'{ticket.requester_name.upper()}')
        p.drawCentredString(x=min_x+432, y=78, text=f'{ticket.response_user.upper()}')

        p.drawString(x=min_x+50, y=40, text=f'{datetime.now().strftime("%A, %d, de %B de %Y")}')

        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f'ticket_{ticket.id}.pdf')

    return render(request, 'app_ticket/single_ticket.html', {
        'ticket': ticket, 'users':users
    })

