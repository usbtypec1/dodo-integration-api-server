# Generated by Django 5.2 on 2025-04-06 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        ('telegram', '0001_initial'),
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportroute',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_routes', to='telegram.telegramchat', verbose_name='Telegram chat'),
        ),
        migrations.AddField(
            model_name='reportroute',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_routes', to='units.unit', verbose_name='Unit'),
        ),
        migrations.AddField(
            model_name='reportroute',
            name='report_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_routes', to='reports.reporttype', verbose_name='Report type'),
        ),
        migrations.AddField(
            model_name='reporttype',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_types', to='reports.reporttypegroup', verbose_name='Report type group'),
        ),
        migrations.AddConstraint(
            model_name='reportroute',
            constraint=models.UniqueConstraint(fields=('chat', 'unit', 'report_type'), name='unique_report_route'),
        ),
    ]
