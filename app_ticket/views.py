from unicodedata import category
from django.shortcuts import render
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

    return render(request, 'app_ticket/ticket_form.html', data)