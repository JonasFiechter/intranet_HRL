from django.forms import ModelForm, Textarea
from .models import Ticket
from django.contrib.auth.models import User


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['description', 'sector', 'machine_number', 'requester_name', 
        'patrimony', 'response_user', 'serial_number', 'machine_description',
        'phone_branch', 'room_number']
        widgets = {
          'description': Textarea(attrs={'rows':4, 'cols':50}),
          'requester_name': Textarea(attrs={'rows':1, 'cols':50}),
        }

class UserForm(ModelForm):
    class Meta:
      model = User
      fields = ['first_name', 'last_name', 'groups']