from tabnanny import verbose
from django.db import models

# Create your models here.

class Sector(models.Model):
    sector_name = models.CharField(verbose_name='Setor', max_length=100)

    def __str__(self) -> str:
        return str(self.sector_name)

    class Meta:
        verbose_name_plural = 'Setores'


class MachineType(models.Model):
    machine_name = models.CharField(verbose_name='Máquinas Hospitalares', max_length=100)

    def __str__(self) -> str:
        return str(self.machine_name)

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


class TransportRequest(models.Model):

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name_plural = 'Chamados para Transporte'
    
    t_open = 'Aberto'
    t_answered = 'Atendido'
    t_closed = 'Finalizado'

    status = models.CharField(max_length=100,
                              choices=[(t_open, 'Aberto'),
                                       (t_answered,'Atendido'),
                                       (t_closed,'Finalizado')], default=t_open)

    description = models.TextField(verbose_name='Descrição', max_length=500, null=True)
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    requester_name = models.CharField(verbose_name='Requisitante', max_length=255)
    sector = models.ForeignKey(Sector, verbose_name='Setor', on_delete=models.DO_NOTHING, null=True)
    response_user = models.CharField(verbose_name='Responsável', max_length=255, null=True)
    phone_branch = models.CharField(verbose_name='Ramal', max_length=255, null=True)
    destination_address = models.CharField(verbose_name='Endereço de destino', max_length=500, null=True)
    local_number = models.IntegerField(verbose_name='Nº da rua', null=True)
    quarter_name = models.CharField(verbose_name='Bairro de destino', max_length=255, null=True)
    city_name = models.CharField(verbose_name='Cidade de destino', max_length=255, null=True)
    departure_date = models.CharField(verbose_name='Data de saída', max_length=255, null=True)
    departure_hour = models.CharField(verbose_name='Hora de partida', max_length=100, null=True)
    destination_contact = models.CharField(verbose_name='Contato no destino',max_length=255, null=True)
    contact_phone = models.CharField(verbose_name='Telefone do contato', max_length=255, null=True)
    transport_type = models.CharField(verbose_name='Tipo de transporte', max_length=255, null=True)
    patient_name = models.CharField(verbose_name='Nome do paciente', max_length=255, null=True)
    patient_age = models.IntegerField(verbose_name='Idade do paciente', null=True)
    category = models.CharField(verbose_name='Setor responsável', max_length=255, null=True)