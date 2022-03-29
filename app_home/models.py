from django.db import models
from app_ticket.models import Sector

# Create your models here.
class PhoneExtensions(models.Model):

    class Meta:
        verbose_name_plural = 'Ramais'
    
    branch = models.IntegerField(verbose_name='Ramal', null=True)
    sector = models.ForeignKey(Sector,verbose_name='Setor',  on_delete=models.DO_NOTHING)
    floor = models.IntegerField(verbose_name='Andar', null=True)
    description = models.TextField(verbose_name='Descrição', max_length=255, null=True)