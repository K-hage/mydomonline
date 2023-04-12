from django.db import models


class Entity(models.Model):
    modified_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Редактор',
        help_text='Укажите редактора'
    )
    value = models.IntegerField(
        verbose_name='Значение',
        help_text='Укажите значение'
    )
    properties = models.ManyToManyField(
        'core.Property',
        related_name='properties',
        help_text='Укажите свойства'
    )


class Property(models.Model):
    key = models.CharField(
        verbose_name='Ключ',
        max_length=50,
        help_text='Укажите ключ',
    )
    value = models.CharField(
        verbose_name='Значение',
        max_length=50,
        help_text='Укажите значение',
    )
