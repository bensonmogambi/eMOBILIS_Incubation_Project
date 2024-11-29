# Generated by Django 2.1.2 on 2018-11-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='abc', max_length=20, verbose_name='user_name')),
                ('user_first_name', models.CharField(default='Chaman', max_length=15, verbose_name='Enter first name')),
                ('user_last_name', models.CharField(default='Chaman', max_length=15, verbose_name='Enter first name')),
                ('user_phone', models.CharField(default='', max_length=10, verbose_name='cellphone number')),
                ('user_site_address', models.CharField(default='not assigned', max_length=10, verbose_name='Site Address')),
            ],
            options={
                'verbose_name': 'Employee Data  ',
                'verbose_name_plural': ' Employee Data',
            },
        ),
    ]
