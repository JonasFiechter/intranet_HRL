# Generated by Django 4.0.1 on 2022-05-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_file_storage', '0005_alter_messages_file_alter_messages_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visível'),
        ),
    ]