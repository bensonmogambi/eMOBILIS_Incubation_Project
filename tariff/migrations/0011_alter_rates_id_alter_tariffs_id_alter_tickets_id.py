# Generated by Django 5.1.3 on 2024-11-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0010_auto_20181216_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
