from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('електронна адреса'), unique=True)
    phone_number = models.CharField(_('номер телефону'), max_length=13, unique=True)
    first_name = models.CharField(_("ім'я"), max_length=30, blank=True)
    last_name = models.CharField(_('прізвище'), max_length=30, blank=True)
    patronymic = models.CharField(_('по-батькові'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('дата приєднання'), auto_now_add=True, editable=True)
    is_staff = models.BooleanField(_('суперкористувач'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name', 'patronymic']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Card(models.Model):
    title = models.TextField(_('назва картки'), max_length=100)
    account_iban = models.TextField(_('iban'), max_length=29)
    card_number = models.TextField(_('номер картки'), max_length=19, primary_key=True, unique=True)
    expiry_date = models.TextField(_('термін дії'), max_length=5)
    cvv = models.TextField(max_length=3)
    cardholder_name = models.TextField(_("ім'я власника картки"), max_length=100)
    cardholder_surname = models.TextField(_('прізвище власника картки'), max_length=100)
    cardholder_email = models.EmailField(_('електронна адреса'), null=True)

    class Meta:
        verbose_name = _('картка')
        verbose_name_plural = _('картки')

    def get_number_last_digits(self):
        return self.card_number[14:18]


class BankAccount(models.Model):
    name = models.TextField(_("ім'я власника рахунку"), max_length=100)
    surname = models.TextField(_('прізвище власника рахунку'), max_length=100)
    patronymic = models.TextField(_('по-батькові власника рахунку'), max_length=100)
    iban = models.TextField(_('iban'), max_length=29, primary_key=True, unique=True)
    currency = models.TextField()
    money = models.TextField()
    email = models.EmailField(_('електронна адреса'), null=True)

    class Meta:
        verbose_name = _('банківський рахунок')
        verbose_name_plural = _('банківські рахунки')
