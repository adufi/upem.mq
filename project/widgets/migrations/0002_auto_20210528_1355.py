# Generated by Django 2.2.19 on 2021-05-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='label',
            field=models.TextField(blank=True, default='', verbose_name='Nom aternatif'),
        ),
    ]