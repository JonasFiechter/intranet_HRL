from tabnanny import verbose
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


class FunctionsBySector(models.Model):

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Funções setoriais'
    
    branch = models.IntegerField(verbose_name='Ramal', null=True)
    name = models.CharField(verbose_name='Nome da atividade', max_length=255, null=True)
    description = models.TextField(verbose_name='Descrição', null=True)
    sector = models.ForeignKey(Sector, verbose_name='Setor', on_delete=models.DO_NOTHING)
