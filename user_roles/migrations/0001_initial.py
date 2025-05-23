# Generated by Django 5.2 on 2025-04-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Role name')),
                ('access_code', models.CharField(max_length=255, unique=True, verbose_name='Access code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('report_types', models.ManyToManyField(to='reports.reporttype', verbose_name='Report types')),
                ('units', models.ManyToManyField(to='units.unit', verbose_name='Units')),
            ],
            options={
                'verbose_name': 'User role',
                'verbose_name_plural': 'User roles',
            },
        ),
    ]
