from importlib.metadata import files
from statistics import median
from django.shortcuts import render
from .models import Messages
import os

# Create your views here.

def messages_view(request, navigation):
    #  Here is a test trying to render the folders and files in a path that could be
    # passed as a request throught the url

    if navigation == 'root':
        navigation = ''
    
    print(navigation)

    dirs = []
    root_dir = r'./media/files'

    for root, _dirs, files in os.walk(root_dir + '/' + navigation):
        dirs = [d for d in _dirs]
        files = [f for f in files]
        break
    
    print(dirs)

    messages = Messages.objects.all()
    for message in messages:
        message.file = '/media/' + str(message.file)

    return render(request, 'app_file_storage/test.html', {'messages': messages, 
                                                          'dirs':dirs,
                                                          'files':files,})