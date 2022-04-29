from ast import Try
from datetime import date, datetime
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título', null=True)
    description = models.TextField(verbose_name='Descritivo', null=True)
    author = models.CharField(max_length=255, verbose_name='Autor', null=True)
    date = models.DateTimeField(verbose_name='Data', auto_now_add=datetime.now, null=True)
    img = models.ImageField(upload_to='post_img/%Y/%m/%d/', null=True)