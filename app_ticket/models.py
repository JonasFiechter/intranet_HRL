from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Sector(models.Model):
    sector_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.sector_name


class Ticket(models.Model):

    def __str__(self) -> str:
        return self.description

    t_open = 't_open'
    t_answered = 't_answered'
    t_closed = 't_closed'

    status = models.CharField(max_length=100,
                              choices=[(t_open, 'aberto'),
                                       (t_answered,'atendido'),
                                       (t_closed,'finalizado')], default=t_open)

    description = models.TextField(max_length=500, )
    date = models.DateTimeField(auto_now_add=True)
    requester_name = models.CharField(max_length=255)
    machine_number = models.IntegerField()
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


