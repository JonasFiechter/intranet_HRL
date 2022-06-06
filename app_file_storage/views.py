from logging import root
from django.shortcuts import render, redirect
from .models import Messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .components.files_walker import files_walker, files_walker_2

# Create your views here.

def files_view_test(request):
    root_dir = r'./media'

    try:
        folder = request.GET['f']
    except:
        folder = ''
        last_dir = ''

    # dirs, files, last_dir, history = files_walker(root_dir, last_dir='blank', next_dir='root')
    dirs, files, last_dir, history = files_walker_2(root_dir, folder=folder, last_dir=last_dir)

    return render(request, 'app_file_storage/test.html', {'dirs': dirs,
                                                          'files': files,
                                                          'last_dir': last_dir,
                                                          'history': history})


def messages_view(request):
    messages = Messages.objects.all().order_by('-id')
    for message in messages:
        message.file = '/media/' + str(message.file)

    return render(request, 'app_file_storage/messages.html', {'messages': messages, })


@login_required(redirect_field_name='url_login')
def messages_admin_view(request):

    #  Check if the group below is linked to the active user
    if request.user.groups.filter(name='GROUP-QUALIDADE').exists():
        return render(request, 'app_file_storage/messages_admin.html')

    else:
        messages.error(
            request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')
