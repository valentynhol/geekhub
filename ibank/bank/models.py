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
    title = models.CharField(_('назва картки'), max_length=100, default='Картка')
    bank_account = models.BigIntegerField(_('банківський рахунок'), null=True)
    card_number = models.CharField(_('номер картки'), max_length=19, unique=True)
    expiry_date = models.CharField(_('термін дії'), max_length=5)
    payment_system = models.CharField(_('платіжна система'), choices=[('visa', 'Visa'), ('mastercard', 'Mastercard')],
                                      max_length=10)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(_("ім'я власника картки"), max_length=30)
    cardholder_surname = models.CharField(_('прізвище власника картки'), max_length=30)
    cardholder_email = models.EmailField(_('електронна адреса власника картки'), null=True)
    color = models.CharField(_('колір картки'), choices=[('blue', 'Cиній'), ('cyan', 'Бірюзовий'), ('green', 'Зелений'),
                             ('grey', 'Сірий'), ('magenta', 'Пурпурний'), ('orange', 'Оранжевий'),
                             ('purple', 'Фіолетовий'), ('red', 'Червоний'), ('yellow', 'Жовтий')], max_length=9,
                             default='blue')

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = _('картка')
        verbose_name_plural = _('картки')


class BankAccount(models.Model):
    title = models.CharField(_("назва банківського рахунку"), max_length=100, default='Картка')
    name = models.CharField(_("ім'я власника рахунку"), max_length=30)
    surname = models.CharField(_('прізвище власника рахунку'), max_length=30)
    patronymic = models.CharField(_('по-батькові власника рахунку'), max_length=30)
    iban = models.CharField(_('iban'), max_length=29, unique=True)
    currency = models.CharField(_('валюта'), max_length=3)
    balance = models.CharField(_('баланс'), max_length=100)
    email = models.EmailField(_('електронна адреса'), null=True)

    def __str__(self):
        return self.iban

    class Meta:
        verbose_name = _('банківський рахунок')
        verbose_name_plural = _('банківські рахунки')
