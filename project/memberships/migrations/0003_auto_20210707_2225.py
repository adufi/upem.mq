# Generated by Django 2.2.19 on 2021-07-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_registrationpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationpage',
            name='template',
        ),
        migrations.AddField(
            model_name='registrationpage',
            name='template_credentials',
            field=models.CharField(default='memberships/credentials_page.html', max_length=125),
        ),
        migrations.AddField(
            model_name='registrationpage',
            name='template_memberships',
            field=models.CharField(default='memberships/memberships_page.html', max_length=125),
        ),
    ]