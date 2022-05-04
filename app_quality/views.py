from datetime import date
import re
from django.shortcuts import render, redirect
from app_file_storage.models import Messages
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NotificationForm

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
    form = NotificationForm(request.POST or None)
    is_valid = False
    date = '2010-10-10'

    if request.POST.get('expiration-date'):
        date = request.POST.get('expiration-date')

    if request.method == 'POST':
        try:
            notification = Notification.objects.create(name=request.POST.get('name'),
                                            phone=request.POST.get('phone'),
                                            function=request.POST.get('function'),
                                            sector=request.POST.get('sector'),
                                            date=request.POST.get('date'),
                                            patient_name=request.POST.get('patient-name'),
                                            chart_number=request.POST.get('chart-number'),
                                            description=request.POST.get('description'),
                                            product_name=request.POST.get('product-name'),
                                            brand_manufacturer=request.POST.get('brand-manufacturer'),
                                            batch=request.POST.get('batch'),
                                            expiration_date=date,)

            id_ = notification.id
            print(id_)
            is_valid = True
            notification.save()
            messages.success(request, message=f'{id_}')
            return render(request, 'app_quality/notification_form.html', {'is_valid': is_valid,
                                                                          'messages': messages,
                                                                          'id_': id_})
        except:
            pass
    return render(request, 'app_quality/notification_form.html', {'form': form})