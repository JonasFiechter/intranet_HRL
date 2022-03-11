"""intranet_2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_home.views import home_view
from app_ticket.views import ticket_center_view_ti, ticket_center_view_ti_history, ticket_view_form_ti, \
ticket_view_form_infraestrutura, ticket_single_view
from app_accounts.views import accounts_login_view, accounts_logout_view, accounts_dashboard_view, \
accounts_signup_view


urlpatterns = [
    path('intranet/', home_view, name='url_home'),
    path('admin/', admin.site.urls),
    path('ticket_center_ti/', ticket_center_view_ti, name='url_ticket_center_ti'),
    path('ticket_center_ti_history/', ticket_center_view_ti_history, name='url_ticket_center_ti_history'),
    path('ticket_form_ti/', ticket_view_form_ti, name='url_ticket_form_ti'),
    path('ticket_form_infra/', ticket_view_form_infraestrutura, name='url_ticket_form_infraestrutura'),
    path('<int:ticket_id>', ticket_single_view, name='url_single_ticket'),
    path('accounts/login/', accounts_login_view, name='url_login'),
    path('logout/', accounts_logout_view, name='url_logout'),
    path('dashboard/', accounts_dashboard_view, name='url_dashboard'),
    path('signup/', accounts_signup_view, name='url_signup'),
]