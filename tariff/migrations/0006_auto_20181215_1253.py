# Generated by Django 2.1.4 on 2018-12-15 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0005_auto_20181214_1249'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tickets',
        ),
        migrations.RemoveField(
            model_name='tariffs',
            name='ticket_type',
        ),
    ]
