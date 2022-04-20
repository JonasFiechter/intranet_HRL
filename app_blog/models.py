from datetime import date, datetime
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.TextField(verbose_name='Descritivo')
    author = models.CharField(max_length=255, verbose_name='Autor')
    date = models.DateTimeField(verbose_name='Data', auto_now_add=datetime.now)