# Generated by Django 4.0.1 on 2022-03-30 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ticket', '0041_machinetype_alter_ticket_machine_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machinetype',
            old_name='sector_name',
            new_name='machine_name',
        ),
    ]