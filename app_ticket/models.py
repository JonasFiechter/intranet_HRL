from django.db import models

# Create your models here.

class Sector(models.Model):
    sector_name = models.CharField(max_length=100, default='.')

    def __str__(self) -> str:
        return self.sector_name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING, default=1)

    def __str__(self) -> str:
        return self.name + f' ({self.description})'

    class Meta:
        verbose_name_plural = "categories"


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
    machine_number = models.IntegerField()
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)