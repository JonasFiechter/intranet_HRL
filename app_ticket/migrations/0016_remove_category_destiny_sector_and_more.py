# Generated by Django 4.0.1 on 2022-02-17 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ticket', '0015_category_destiny_sector_alter_category_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='destiny_sector',
        ),
        migrations.AddField(
            model_name='category',
            name='destiny_sector',
            field=models.ManyToManyField(to='app_ticket.Sector'),
        ),
    ]
