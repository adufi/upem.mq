from __future__ import unicode_literals

import threading

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet

from .managers import AuthManager
from core.models import SEOPage


class EmailThread (threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run (self):
        self.email.send(fail_silently=False)
    

@register_snippet
class Auth (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(_('active'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Est administrateur ?')

    objects = AuthManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    panels = [
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('password'),
            FieldPanel('is_superuser')
        ], heading='Authentification')
    ]

    class Meta:
        verbose_name = _('auth')
        verbose_name_plural = _('auths')

    def save (self, *args, **kwargs):
        self.set_password(self.password)
        super(AbstractBaseUser, self).save(*args, **kwargs)


class LoginPage (SEOPage):
    template = 'user/login_page.html'
    landing_page_template = 'user/login_page_landing.html'

    class Meta:
        verbose_name = 'Auth: Connexion'

    def serve (self, request, *args, **kwargs):
        template = self.template
        context = self.get_context (request)

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            logout (request)
            auth = authenticate(email=email, password=password)

            if auth is not None:
                login (request, auth)
                template = self.landing_page_template

            else:
                context['email'] = email
                context['message'] = 'Les identifiants sont invalides.'

        return render (
            request,
            template,
            context
        )


class ForgotPage (Page):
    template = 'user/login_page.html'
    landing_page_template = 'user/login_page_landing.html'

    class Meta:
        verbose_name = 'Auth: Connexion'

    def serve (self, request, *args, **kwargs):
        template = self.template
        context = self.get_context (request)

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            logout (request)
            auth = authenticate(email=email, password=password)

            if auth is not None:
                login (request, auth)
                template = self.landing_page_template

            else:
                context['email'] = email
                context['message'] = 'Les identifiants sont invalides.'

        return render (
            request,
            template,
            context
        )


class LoginLandingPage (SEOPage):
    template = 'user/login_page_landing.html'

    class Meta:
        verbose_name = 'Auth: Connexion - Landing Test'


class LogoutPage (Page):
    class Meta:
        verbose_name = 'Auth: Deconnexion'

    def serve(self, request, *args, **kwargs):
        logout(request)
        return render (
            request,
            self.get_template(request, *args, **kwargs),
            {}
        )


class UnauthorizedPage (Page):
    class Meta:
        verbose_name = 'Auth: Accès non autorisé'


# class Person (models.Model):
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#     auth = models.ForeignKey(
#         Auth,
#         related_name='auth',
#         on_delete=models.CASCADE
#     )

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)
