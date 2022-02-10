from django.shortcuts import render

# Create your views here.

def ticket_view_a(request):
    return render(request, 'app_ticket/ticket.html')


def ticket_view_b(request):
    return render(request, 'app_ticket/ticket_form.html')