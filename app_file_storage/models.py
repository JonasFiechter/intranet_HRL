from django.db import models
from filer.fields.file import FilerFileField

# Create your models here.

class Messages(models.Model):
    
    class Meta:
        verbose_name_plural = 'Messages'

    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/messages/%Y', null=True)