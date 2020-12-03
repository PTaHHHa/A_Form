from django.db import models

# Create your models here.


class CitizenAppeal(models.Model):
    FIO = models.CharField(max_length=120, unique=False, blank=True, null=True, verbose_name='Фамилия Имя Отчество')
    organisation = models.CharField(max_length=50, blank=True, null=True, verbose_name='Наименование организации')
    address = models.CharField(max_length=120, blank=False, null=True, verbose_name='Адрес')
    email = models.EmailField(max_length=120, blank=False, null=True, verbose_name='Email для обратной связи')
    text = models.TextField(max_length=900, blank=False, null=True, verbose_name='Сообщение для нас')
