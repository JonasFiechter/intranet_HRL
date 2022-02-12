from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['description', 'category', 'sector', 'machine_number', 'requester_name']