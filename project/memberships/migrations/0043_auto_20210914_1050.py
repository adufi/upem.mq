# Generated by Django 2.2.19 on 2021-09-14 14:50

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0042_auto_20210914_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberapplicationorderable',
            name='application',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_lists', to='memberships.MemberApplication'),
        ),
    ]