# Generated by Django 4.0.1 on 2022-02-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ticket', '0026_ticket_patrimony'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='patrimony',
            field=models.CharField(max_length=255),
        ),
    ]
