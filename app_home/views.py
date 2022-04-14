from django.shortcuts import render, redirect
from .models import PhoneExtensions, FunctionsBySector

# Create your views here.

def home_view(request):
    return render(request, 'app_home/home.html')

def phone_extensions_view(request):
    branches = PhoneExtensions.objects.all()
    return render(request, 'phone_extensions/phone_extensions.html', {'branches': branches})

def help_me_view(request):
    functions = FunctionsBySector.objects.all()

    for function in functions:
        print(function.sector.sector_name)

    return render(request, 'help_me/help_me.html', {
        'functions': functions
    })