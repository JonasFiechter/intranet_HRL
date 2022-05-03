from django.shortcuts import render, redirect
from app_file_storage.models import Messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(redirect_field_name='url_login')
def quality_admin_view(request):
    if request.user.groups.filter(name='GROUP-QUALIDADE').exists():
        _messages = Messages.objects.order_by('-id')
        return render(request, 'app_quality/quality_admin.html')
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')


def notification_form_view(request):
    return render(request, 'app_quality/notification_form.html')