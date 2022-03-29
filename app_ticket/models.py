from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sector(models.Model):
    sector_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.sector_name


class Ticket(models.Model):

    def __str__(self) -> str:
        return self.description

    t_open = 'Aberto'
    t_answered = 'Atendido'
    t_closed = 'Finalizado'

    status = models.CharField(max_length=100,
                              choices=[(t_open, 'Aberto'),
                                       (t_answered,'Atendido'),
                                       (t_closed,'Finalizado')], default=t_open)

    description = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    requester_name = models.CharField(max_length=255)
    machine_number = models.IntegerField(null=True)
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=255)
    patrimony = models.CharField(max_length=255)
    response_user = models.CharField(max_length=255, null=True)
    serial_number = models.CharField(max_length=255, null=True)
    machine_description = models.CharField(max_length=255, null=True)
    phone_branch = models.CharField(max_length=255, null=True)
    room_number = models.CharField(max_length=255, null=True)


class DriversTicket(models.Model):

    def __str__(self):
        return self.description

    pass    