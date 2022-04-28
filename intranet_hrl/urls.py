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
from app_home.views import *
from app_ticket.views import *
from app_accounts.views import *
from app_blog.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from app_file_storage.views import messages_view

urlpatterns = [
    path('intranet/', home_view, name='url_home'),
    path('', home_view, name='url_home'),
    path('admin/', admin.site.urls),
    path('ticket_center_it/', ticket_center_view_it, name='url_ticket_center_it'),
    path('ticket_center_infra/', ticket_center_view_infra, name='url_ticket_center_infra'),
    path('ticket_center_patrimony/', ticket_center_view_patrimony, name='url_ticket_center_patrimony'),
    path('ticket_center_roomcare/', ticket_center_view_roomcare, name='url_ticket_center_roomcare'),
    path('ticket_center_it_history/', ticket_center_view_it_history, name='url_ticket_center_it_history'),
    path('ticket_center_infra_history/', ticket_center_view_infra_history, name='url_ticket_center_infra_history'),
    path('ticket_center_patrimony_history/', ticket_center_view_patrimony_history, name='url_ticket_center_patrimony_history'),
    path('ticket_center_roomcare_history/', ticket_center_view_roomcare_history, name='url_ticket_center_roomcare_history'),
    path('ticket_center_transport/', ticket_center_view_transport, name='url_ticket_center_transport'),
    path('ticket_center_transport_history/', ticket_center_view_transport_history, name='url_ticket_center_transport_history'),
    path('ticket_center_clinical_engeneering/', ticket_center_view_clinical_engeneering, name='url_ticket_center_clinical_engeneering'),
    path('ticket_center_clinical_engeneering_history/', ticket_center_view_clinical_engeneering_history, name='url_ticket_center_clinical_engeneering_history'),
    path('ticket_form_it/', ticket_view_form_it, name='url_ticket_form_it'),
    path('ticket_form_infra/', ticket_view_form_infra, name='url_ticket_form_infra'),
    path('ticket_form_patrimony/', ticket_view_form_patrimony, name='url_ticket_form_patrimony'),
    path('ticket_form_clinical_engeneering/', ticket_view_form_clinical_engeneering, name='url_ticket_form_clinical_engeneering'),
    path('ticket_form_telephony/', ticket_view_form_telephony, name='url_ticket_form_telephony'),
    path('ticket_form_roomcare/', ticket_view_form_roomcare, name='url_ticket_form_roomcare'),
    path('ticket_form_transport/', ticket_view_form_transport, name='url_ticket_form_transport'),
    path('<int:ticket_id>/<str:ticket_type>', ticket_single_view, name='url_single_ticket'),
    path('accounts/login/', accounts_login_view, name='url_login'),
    path('logout/', accounts_logout_view, name='url_logout'),
    path('dashboard/', accounts_dashboard_view, name='url_dashboard'),
    path('signup/', accounts_signup_view, name='url_signup'),
    path('phone_extensions/', phone_extensions_view, name='url_phone_extensions'),
    path('help_me/', help_me_view, name='url_help_me'),
    path('summernote/', include('django_summernote.urls')),
    path('messages_test/<str:last_dir>/<str:next_dir>', messages_view, name='url_messages_test'),
    path('filer/', include('filer.urls')),
    path('messages/', messages_view, name='url_messages'),
]

# This line creates a new path with the file name as a url to render in the html
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)