# Generated by Django 4.0.1 on 2022-02-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ticket', '0024_alter_ticket_machine_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='sector_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]