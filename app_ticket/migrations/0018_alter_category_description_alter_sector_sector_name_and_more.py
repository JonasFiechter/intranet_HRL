# Generated by Django 4.0.1 on 2022-02-17 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ticket', '0017_alter_sector_sector_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=500),
        ),
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
    ]
