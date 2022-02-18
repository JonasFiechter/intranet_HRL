from unicodedata import category
from django.forms import ModelForm, Textarea
from .models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['description', 'sector', 'machine_number', 'requester_name', 'category']
        widgets = {
          'description': Textarea(attrs={'rows':4, 'cols':50}),
          'requester_name': Textarea(attrs={'rows':1, 'cols':50}),
        }