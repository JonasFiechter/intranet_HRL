from django.db import models
from app_ticket.models import Sector

# Create your models here.

class Notification(models.Model):
    name = models.CharField(verbose_name='Nome do Notificante', max_length=255, null=True, blank=True)
    date = models.DateTimeField(verbose_name='Data')
    phone = models.CharField(verbose_name='Telefone', max_length=255, null=True, blank=True)
    function = models.CharField(verbose_name='Cargo/Função', max_length=255, null=True, blank=True)
    sector = models.CharField(verbose_name='Setor', max_length=255, null=True, blank=True)
    patient_name = models.CharField(verbose_name='Nome do paciente', max_length=255, null=True, blank=True)
    chart_number = models.CharField(verbose_name='Nº do prontuário', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    product_name = models.CharField(verbose_name='Nome do produto', max_length=255)
    brand_manufacturer = models.CharField(verbose_name='Marca/Fabricante', max_length=255, blank=True, null=True)
    batch = models.CharField(verbose_name='Lote', max_length=255, default='none', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='Data de validade', null=True, blank=True)