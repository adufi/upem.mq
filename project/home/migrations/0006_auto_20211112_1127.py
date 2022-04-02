# Generated by Django 3.2.7 on 2021-11-12 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210927_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoAreWePageTile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('icon', models.CharField(default='', max_length=128, verbose_name='Icon')),
                ('title', models.CharField(default='', max_length=128, verbose_name='Titre')),
                ('text', models.CharField(default='', max_length=255, verbose_name='Contenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='whoarewepage',
            name='tile_main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tiles_main', to='home.whoarewepagetile'),
        ),
        migrations.AddField(
            model_name='whoarewepage',
            name='tile_sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tiles_sub', to='home.whoarewepagetile'),
        ),
    ]