# Generated by Django 2.2.19 on 2021-09-09 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0036_membercontribution_transaction_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'ordering': ['-date_end'], 'verbose_name': 'Cotisation'},
        ),
        migrations.AlterField(
            model_name='membercontribution',
            name='date_bought',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date achat'),
        ),
    ]
