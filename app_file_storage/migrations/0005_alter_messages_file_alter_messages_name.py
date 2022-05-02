# Generated by Django 4.0.1 on 2022-05-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_file_storage', '0004_alter_messages_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='file',
            field=models.FileField(null=True, upload_to='files/messages/%Y/%m', verbose_name='Anexo'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Assunto'),
        ),
    ]
