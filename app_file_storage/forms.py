from django.forms import ModelForm
from .models import Messages

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'sector', 'file']