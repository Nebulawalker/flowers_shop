# Generated by Django 4.2.4 on 2023-08-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop_site', '0004_order_is_notification_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquet',
            name='size',
            field=models.TextField(default='Высота - 50 см\nШирина - 30 см', verbose_name='Размер букета'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True, verbose_name='Название в виде url'),
        ),
    ]