from django import forms
from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from widgets.models import Alert, IconBox

from core.models import SEOPage


""" Used as Index Page """
class BlankIndexPage (SEOPage):

    class Meta:
        verbose_name = 'Template: Index'


""" Used as a free page with customizable template path """
class FreeHTMLPage (SEOPage):
    template = models.CharField(max_length=125, default='home/free_html_page.html')

    promote_panels = SEOPage.promote_panels + [
        FieldPanel('template')
    ]

    class Meta:
        verbose_name = 'Template: Page'


class HomePage(SEOPage):
    body = RichTextField(blank=True)

    icon_boxes = ParentalManyToManyField(
        IconBox,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
        InlinePanel('gallery_images', label='Gallery images'),
        FieldPanel('icon_boxes', heading='Icon Boxes', widget=forms.CheckboxSelectMultiple)
    ]

    @property
    def alerts (self):
        return Alert.objects.active()

    def foo (self):
        return ['Hello', 'World']

    def serve (self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['foo'] = 'bar'
        
        return render (
            request,
            self.get_template(request, *args, **kwargs),
            context
        )


class HomeCarousel(Orderable):
    home = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    link = models.URLField(blank=True, default='', verbose_name='URL')

    caption = RichTextField(blank=True, max_length=250, verbose_name='Courte introduction')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('link'),
    ]


class WhoAreWeTileMain (Orderable):
    page = ParentalKey(
        'home.WhoAreWePage',
        related_name='tiles_main'
    )

    icon = models.CharField(
        max_length=128, 
        default='', 
        verbose_name='Icon classe',
        help_text='Liste disponible sur: https://semantic-ui.com/elements/icon.html'
    )
    
    title = models.CharField(max_length=128, default='', verbose_name='Titre')
    content = models.CharField(max_length=255, default='', verbose_name='Contenu')

    panels = [
        FieldPanel('icon'),
        FieldPanel('title'),
        FieldPanel('content')
    ]


class WhoAreWeTileSub (Orderable):
    page = ParentalKey(
        'home.WhoAreWePage',
        related_name='tiles_sub'
    )

    icon = models.CharField(
        default='', 
        max_length=128, 
        verbose_name='Icon classe', 
        help_text='Liste disponible sur: https://semantic-ui.com/elements/icon.html'
    )

    title = models.CharField(max_length=128, default='', verbose_name='Titre')
    content = models.CharField(max_length=255, default='', verbose_name='Contenu')

    panels = [
        FieldPanel('icon'),
        FieldPanel('title'),
        FieldPanel('content')
    ]


class WhoAreWePage (SEOPage):
    template = 'home/about_us_page.html'

    history = RichTextField(blank=True, verbose_name='Historique: Contenu')
    history_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='history_image',
        verbose_name='Historique: Image',
        help_text='Dimensions: 500x500'
    )

    quote = RichTextField(blank=True, verbose_name='Citation: citation')
    quote_author = models.CharField(max_length=255, default='', blank=True, verbose_name='Citation: Auteur')
    quote_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='quote_image',
        verbose_name='Citation: Image',
        help_text='Dimensions: Largeur 1920 min.'
    )

    # Replaced by Orderables
    # ...
    # tile_schoo_council = models.CharField(max_length=255, default='', blank=True, verbose_name='Conseil d\'école')
    # tile_class_council = models.CharField(max_length=255, default='', blank=True, verbose_name='Conseil de classe')
    # tile_admin_council = models.CharField(max_length=255, default='', blank=True, verbose_name='Conseil d\'adminstration')
    # tile_disci_council = models.CharField(max_length=255, default='', blank=True, verbose_name='Conseil de discipline')

    # tile_cen = models.CharField(max_length=255, default='', blank=True, verbose_name='Conseil éducation nationale')
    # tile_education = models.CharField(max_length=255, default='', blank=True, verbose_name='Comité éducation santé citoyenneté')
    # tile_languages = models.CharField(max_length=255, default='', blank=True, verbose_name='Commission des langues régionales')
    # tile_scholarships = models.CharField(max_length=255, default='', blank=True, verbose_name='Commission des bourses')

    content_panels = [
        MultiFieldPanel([
            FieldPanel('history'),
            ImageChooserPanel('history_image')
        ], heading='Historique'),
        MultiFieldPanel([
            FieldPanel('quote'),
            FieldPanel('quote_author'),
            ImageChooserPanel('quote_image')
        ], heading='Citation'),
        InlinePanel('tiles_main', max_num=4, label='Tuiles principales'),
        InlinePanel('tiles_sub', max_num=4, label='Tuiles secondaires'),

        # Replaced by Orderables
        # ...
        # MultiFieldPanel([
        #     FieldPanel('tile_schoo_council'),
        #     FieldPanel('tile_class_council'),
        #     FieldPanel('tile_admin_council'),
        #     FieldPanel('tile_disci_council'),
        # ], heading='Principales'),
        # MultiFieldPanel([
        #     FieldPanel('tile_education'),
        #     FieldPanel('tile_cen'),
        #     FieldPanel('tile_languages'),
        #     FieldPanel('tile_scholarships'),
        # ], heading='Secondaires'),
    ]

    class Meta:
        verbose_name = 'Qui sommes-nous ?'


# consectetur adipiscing elit. 
# Quisque tempus justo vel velit porttitor posuere. 
# Curabitur sed turpis sit amet sem pellentesque tincidunt.