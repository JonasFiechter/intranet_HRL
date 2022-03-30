from django.db import models

# Create your models here.

class Sector(models.Model):
    sector_name = models.CharField(verbose_name='Setor', max_length=100)

    def __str__(self) -> str:
        return self.sector_name

    class Meta:
        verbose_name_plural = 'Setores'


class MachineType(models.Model):
    machine_name = models.CharField(verbose_name='Máquinas Hospitalares', max_length=100)

    def __str__(self) -> str:
        return self.machine_name

    class Meta:
        verbose_name_plural = 'Máquinas Hospitalares'


class Ticket(models.Model):

    def __str__(self) -> str:
        return self.description
    
    class Meta:
        verbose_name_plural = 'Chamados'

    t_open = 'Aberto'
    t_answered = 'Atendido'
    t_closed = 'Finalizado'

    status = models.CharField(max_length=100,
                              choices=[(t_open, 'Aberto'),
                                       (t_answered,'Atendido'),
                                       (t_closed,'Finalizado')], default=t_open)

    description = models.TextField(verbose_name='Descrição', max_length=500)
    date = models.DateTimeField(verbose_name='Data',auto_now_add=True)
    requester_name = models.CharField(verbose_name='Requisitante', max_length=255)
    machine_number = models.IntegerField(verbose_name='Número da máquina', null=True)
    sector = models.ForeignKey(Sector, verbose_name='Setor', on_delete=models.DO_NOTHING)
    category = models.CharField(verbose_name='Setor responsável', max_length=255)
    patrimony = models.CharField(max_length=255)
    response_user = models.CharField(verbose_name='Responsável', max_length=255, null=True)
    serial_number = models.CharField(verbose_name='Número de Série', max_length=255, null=True)
    machine_description = models.ForeignKey(MachineType, verbose_name='Tipo da máquina', on_delete=models.DO_NOTHING, max_length=255, null=True)
    phone_branch = models.CharField(verbose_name='Ramal', max_length=255, null=True)
    room_number = models.CharField(verbose_name='Número do quarto', max_length=255, null=True)