from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def accounts_login_view(request):
    return render(request, 'app_accounts/login.html')


def accounts_logout_view(request):
    return render(request, 'app_accounts/logout.html')


def accounts_dashboard_view(request):
    return render(request, 'app_accounts/dashboard.html')


def accounts_signup_view(request):
    if request.method != 'POST':
        return render(request, 'app_accounts/signup.html')

    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, message='Email already exists!')
        return render(request, 'app_accounts/signup.html')

    if password != password2:
        messages.error(request, message="Passwords don't match!")
        return render(request, 'app_accounts/signup.html')

    else:
        messages.success(request, 'Registrado com sucesso! Faça login.')

        user = User.objects.create_user(username=email, 
                                    email=email, 
                                    first_name=first_name,
                                    last_name=last_name,
                                    password=password)

        return redirect('url_login')

    return render(request, 'app_accounts/signup.html')