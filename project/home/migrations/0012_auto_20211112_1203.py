# Generated by Django 3.2.7 on 2021-11-12 16:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0011_rename_text_whoarewetilesub_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_admin_council',
        ),
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_cen',
        ),
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_class_council',
        ),
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_disci_council',
        ),
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_education',
        ),
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_languages',
        ),
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_scholarships',
        ),
        migrations.RemoveField(
            model_name='whoarewepage',
            name='tile_schoo_council',
        ),
        migrations.AddField(
            model_name='whoarewepage',
            name='history_image',
            field=models.ForeignKey(help_text='Dimensions: 500x500', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_image', to='wagtailimages.image', verbose_name='Historique: Image'),
        ),
        migrations.AddField(
            model_name='whoarewepage',
            name='quote_image',
            field=models.ForeignKey(help_text='Dimensions: Largeur 1920 min.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote_image', to='wagtailimages.image', verbose_name='Citation: Image'),
        ),
        migrations.AlterField(
            model_name='whoarewepage',
            name='history',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Historique: Contenu'),
        ),
        migrations.AlterField(
            model_name='whoarewepage',
            name='quote',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Citation: citation'),
        ),
        migrations.AlterField(
            model_name='whoarewepage',
            name='quote_author',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Citation: Auteur'),
        ),
    ]
