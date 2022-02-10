from tabnanny import verbose
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'


class Status(models.Model):  
    t_open = 't_open'
    t_answered = 't_answered'
    t_closed = 't_closed'

    status_name = models.CharField(max_length=100,
                                            choices=[(t_open, 'aberto'),
                                            (t_answered,'atendido'),
                                            (t_closed,'finalizado')])

    class Meta:
        verbose_name_plural = 'Status'


class Ticket(models.Model):
    description = models.TextField(max_length=500)
    date = models.DateTimeField()
    requester_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    machine_number = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
