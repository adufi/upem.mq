# Generated by Django 2.2.19 on 2021-05-28 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0003_auto_20210528_1355'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestSEOPage',
        ),
    ]
