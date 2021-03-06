# Generated by Django 4.0.4 on 2022-05-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do Notificante')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('function', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cargo/Função')),
                ('sector', models.CharField(blank=True, max_length=255, null=True, verbose_name='Setor')),
                ('patient_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do paciente')),
                ('chart_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nº do prontuário')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('product_name', models.CharField(max_length=255, verbose_name='Nome do produto')),
                ('brand_manufacturer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Marca/Fabricante')),
                ('batch', models.CharField(blank=True, default='none', max_length=255, null=True, verbose_name='Lote')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='Data de validade')),
            ],
        ),
    ]
