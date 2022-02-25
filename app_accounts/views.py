from django.shortcuts import render

# Create your views here.

def accounts_login_view(request):
    return render(request, 'app_accounts/login.html')


def accounts_logout_view(request):
    return render(request, 'app_accounts/logout.html')


def accounts_dashboard_view(request):
    return render(request, 'app_accounts/dashboard.html')


def accounts_signup_view(request):
    return render(request, 'app_accounts/signup.html')