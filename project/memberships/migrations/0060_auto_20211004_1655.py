# Generated by Django 3.2.7 on 2021-10-04 20:55

from django.db import migrations, models
import education.models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0059_auto_20211002_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminmembers',
            options={'verbose_name': 'Profile Admin: Membres'},
        ),
        migrations.AlterField(
            model_name='memberchild',
            name='grade',
            field=models.CharField(blank=True, choices=[('Défaut', 'DEFAUT'), ('AUTRE', 'OTHER'), ('Très Petite Section', 'TPS'), ('Petite Section', 'PS'), ('Moyenne Section', 'MS'), ('Grande Section', 'GS'), ('CP', 'CP'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CM1', 'CM1'), ('CM2', 'CM2'), ('6eme', 'C6'), ('5eme', 'C5'), ('4eme', 'C4'), ('3eme', 'C3'), ('2nd', 'L2'), ('1ere', 'L1'), ('Terminale', 'TERM'), ('Etudes', 'UNI')], default=education.models.GradeEnum['DEFAUT'], max_length=20, null=True, verbose_name='Classe'),
        ),
    ]