# Generated by Django 4.0.1 on 2022-04-12 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ticket', '0045_transportrequest_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportrequest',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='transportrequest',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_ticket.sector', verbose_name='Setor'),
        ),
    ]
