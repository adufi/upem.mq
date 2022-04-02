# Generated by Django 3.2.7 on 2021-11-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_whoarewetilesub_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whoarewetilemain',
            old_name='text',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='whoarewetilemain',
            name='icon',
            field=models.CharField(default='', help_text='Liste disponible sur: https://semantic-ui.com/elements/icon.html', max_length=128, verbose_name='Icon classe'),
        ),
        migrations.AlterField(
            model_name='whoarewetilesub',
            name='icon',
            field=models.CharField(default='', help_text='Liste disponible sur: https://semantic-ui.com/elements/icon.html', max_length=128, verbose_name='Icon classe'),
        ),
    ]