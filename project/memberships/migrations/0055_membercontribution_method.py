# Generated by Django 3.2.7 on 2021-09-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0054_auto_20210921_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='membercontribution',
            name='method',
            field=models.CharField(choices=[('ON', 'Online'), ('SO', 'Espèce'), ('JR', 'Chèque'), ('SR', 'Crédit')], default='ON', max_length=2),
        ),
    ]
