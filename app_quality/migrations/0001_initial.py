# Generated by Django 4.0.1 on 2022-05-02 19:18

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
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Nome do Notificante')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('function', models.CharField(max_length=255, verbose_name='Cargo/Função')),
                ('sector', models.CharField(max_length=255, verbose_name='Setor')),
                ('patient_name', models.CharField(max_length=255, verbose_name='Nome do paciente')),
                ('chart_number', models.CharField(max_length=255, verbose_name='Nº do prontuário')),
                ('product_name', models.CharField(max_length=255, verbose_name='Nome do produto')),
                ('brand_manufacturer', models.CharField(max_length=255, verbose_name='Marca/Fabricante')),
                ('batch', models.CharField(max_length=255, verbose_name='Lote')),
                ('expiration_date', models.DateField(verbose_name='Data de validade')),
            ],
        ),
    ]