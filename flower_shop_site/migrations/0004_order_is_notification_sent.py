# Generated by Django 4.2.4 on 2023-08-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop_site', '0003_consultation_is_notification_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_notification_sent',
            field=models.BooleanField(default=False, verbose_name='Отправлено сообщение курьеру'),
        ),
    ]