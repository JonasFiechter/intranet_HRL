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
from app_ticket.views import ticket_center_view_nuias, ticket_view_nuias_form, ticket_view_infra_form

urlpatterns = [
    path('', home_view, name='url_home'),
    path('admin/', admin.site.urls),
    path('ticket_center_nuias/', ticket_center_view_nuias, name='url_ticket_center_nuias'),
    path('ticket_nuias_form/', ticket_view_nuias_form, name='url_ticket_nuias_form'),
    path('ticket_infra_form/', ticket_view_infra_form, name='url_ticket_infra_form'),
]
