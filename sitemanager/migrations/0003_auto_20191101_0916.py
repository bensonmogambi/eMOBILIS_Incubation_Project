# Generated by Django 2.2.6 on 2019-11-01 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0002_auto_20190409_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitemanager',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='Site Manager Bit'),
        ),
    ]