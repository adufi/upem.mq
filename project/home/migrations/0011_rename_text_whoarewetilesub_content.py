# Generated by Django 3.2.7 on 2021-11-12 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211112_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whoarewetilesub',
            old_name='text',
            new_name='content',
        ),
    ]
