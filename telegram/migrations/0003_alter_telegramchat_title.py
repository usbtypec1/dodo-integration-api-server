# Generated by Django 5.2 on 2025-04-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_alter_telegramchat_id_alter_telegramuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramchat',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram title'),
        ),
    ]
