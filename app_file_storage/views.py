from importlib.metadata import files
from statistics import median
from django.shortcuts import render
from .models import Messages
from ..media import *

# Create your views here.

def messages_view(request):
    folder_test = []
    for folder in files:
        print(folder)
    messages = Messages.objects.all()
    for message in messages:
        message.file = '/media/' + str(message.file)

    return render(request, 'app_file_storage/test.html', {'messages': messages})