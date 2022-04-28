from doctest import BLANKLINE_MARKER
from django.db import models
from filer.fields.file import FilerFileField

# Create your models here.

class Messages(models.Model):
    
    class Meta:
        verbose_name_plural = 'Messages'

    name = models.CharField(verbose_name='Assunto', max_length=255)
    file = models.FileField(verbose_name='Anexo', upload_to='files/messages/%Y', null=True)
    sector = models.CharField(verbose_name='Setor', max_length=255, null=True)
    date = models.DateTimeField(verbose_name='Data', auto_now=True)