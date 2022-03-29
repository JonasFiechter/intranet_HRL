from django.shortcuts import render, redirect
from .models import PhoneExtensions

# Create your views here.

def home_view(request):
    return render(request, 'app_home/home.html')

def phone_extensions_view(request):
    branches = PhoneExtensions.objects.all()
    return render(request, 'phone_extensions/phone_extensions.html', {'branches': branches})