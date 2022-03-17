# Generated by Django 4.0.1 on 2022-03-17 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_ticket', '0027_alter_ticket_patrimony'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user_responsible',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]