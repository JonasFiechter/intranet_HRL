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

    print(f'{email}, {first_name}, {last_name}, {password}')

    if len(first_name) == 0 or len(last_name) == 0:
        messages.error(request, message='Digite o seu nome corretamente!')
        return render(request, 'app_accounts/signup.html')

    if len(email) == 0:
        messages.error(request, message='Digite o seu email corretamente!')
        return render(request, 'app_accounts/signup.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, message='Este email já está cadastrado!')
        return render(request, 'app_accounts/signup.html')

    if len(password) < 6 or len(password2) < 6:
        messages.error(request, message='A senha deve conter no mínimo 6 caracteres!')
        return render(request, 'app_accounts/signup.html')

    if password != password2:
        messages.error(request, message="As senhas devem ser iguais!")
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