from django.shortcuts import render, redirect
from .models import Messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .components.files_walker import files_walker

# Create your views here.

def storage_admin_view(request):

    # This method gives to the files_walker method the basic parameters to walk throught the path
    # and unpack the results to pass then throught the render method using dicts.
    # dirs and files are dicts with a dict for each 'dir' or 'file' inside it.
    # see more inside components/files_walker.py

    root_dir = r'./media'
    try:
        path = request.GET['f']
    except:
        path = ''

    dirs, files, history = files_walker(root_dir, path=path)

    return render(request, 'app_file_storage/storage_admin.html', {'dirs': dirs,
                                                                    'files': files,
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
