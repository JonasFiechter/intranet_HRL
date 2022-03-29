from django.shortcuts import render, redirect

# Create your views here.

def home_view(request):
    return render(request, 'app_home/home.html')

def phone_extensions_view(request):
    return render(request, 'phone_extensions/phone_extensions.html')