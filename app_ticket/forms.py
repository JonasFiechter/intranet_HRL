from django.forms import ModelForm, Textarea
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['description', 'category', 'sector', 'machine_number', 'requester_name']
        widgets = {
          'description': Textarea(attrs={'rows':3, 'cols':50}),
        }