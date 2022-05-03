from dataclasses import fields
from django.forms import ModelForm
from .models import Notification
from django.contrib.admin.widgets import AdminDateWidget


# class NotificationForm(ModelForm):
#     class Meta:
#         model = Notification
#         fields = ['date', 'expiration_date']
#         widgets = {
#             'date': AdminDateWidget
#         }