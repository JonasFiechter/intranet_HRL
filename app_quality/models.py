from ssl import VerifyFlags
from tabnanny import verbose
from django.db import models
from app_ticket.models import Sector

# Create your models here.

class Notification(models.Model):
    name = models.CharField(verbose_name='Nome do Notificante', max_length=255, blank=True)
    date = models.DateTimeField(verbose_name='Data')
    phone = models.CharField(verbose_name='Telefone', max_length=255)
    function = models.CharField(verbose_name='Cargo/Função', max_length=255)
    sector = models.CharField(verbose_name='Setor', max_length=255)
    patient_name = models.CharField(verbose_name='Nome do paciente', max_length=255)
    chart_number = models.CharField(verbose_name='Nº do prontuário', max_length=255)
    product_name = models.CharField(verbose_name='Nome do produto', max_length=255)
    brand_manufacturer = models.CharField(verbose_name='Marca/Fabricante', max_length=255)
    batch = models.CharField(verbose_name='Lote', max_length=255)
    expiration_date = models.DateField(verbose_name='Data de validade')