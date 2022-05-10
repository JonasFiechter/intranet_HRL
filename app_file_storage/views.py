from django.shortcuts import render
from .models import Messages
import os
from django.core.paginator import Paginator

# Create your views here.

def files_view_test(request, last_dir, next_dir):

    #  Here is a test trying to render the folders and files in a path that could be
    # passed as a request throught the url

    dirs = []
    files = []
    history = ''
    root_dir = r'./media'

    if next_dir != 'files':
        history = last_dir
        history_list = last_dir.split(':')
        history_last = history_list.pop()
        history = history.replace(f':{history_last}', f'/{history_last}')
        last_dir = last_dir + ':' + next_dir
        next_dir = last_dir.replace(':', '/') + '/'

    for root, _dirs, files in os.walk(root_dir + '/' + next_dir):
        dirs = [d for d in _dirs]
        files = [{'path': str(root[1:] + '/' + f), 'file': f} for f in files]
        # print(f'files > {files} dirs > {dirs} root > {root}')
        break

    return render(request, 'app_file_storage/test.html', {'dirs': dirs,
                                                          'files': files,
                                                          'last_dir': last_dir,
                                                          'history': history})

def messages_view(request):
    messages = Messages.objects.all().order_by('-id')
    for message in messages:
        message.file = '/media/' + str(message.file)

    return render(request, 'app_file_storage/messages.html', {'messages': messages,})


def messages_admin_view(request):
    return render(request, 'app_file_storage/messages_admin.html')