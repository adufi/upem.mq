# Generated by Django 2.2.19 on 2021-08-19 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0033_auto_20210819_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membercontribution',
            name='contribution_plan',
        ),
    ]