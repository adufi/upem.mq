# Generated by Django 2.2.19 on 2021-07-21 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0015_profileaccountpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='auth',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
