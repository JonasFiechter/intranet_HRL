from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

# Create your views here.

def ticket_view_nuias(request):
    data = {'tickets': Ticket.objects.all()}
    return render(request, 'app_ticket/ticket.html', data)


def ticket_view_nuias_form(request):
    form = TicketForm(request.POST or None)
    data = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('url_home')

    return render(request, 'app_ticket/ticket_nuias_form.html', data)


def ticket_view_infra_form(request):
    form = TicketForm(request.Post or None)
    data = {'form': form}

    if form.is_valid():
        form.save()
        print('working')

    return render(request, 'app_ticket/ticket_infra_form.html', data)