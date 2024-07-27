from django.db import models
from django.urls import reverse, NoReverseMatch
from django.core.exceptions import ValidationError


class MenuList(models.Model):
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MenuElements(models.Model):
    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    menu = models.ForeignKey(MenuList, verbose_name='Меню', on_delete=models.CASCADE, default=1)
    name = models.CharField('Категория', max_length=20)
    parent = models.ForeignKey(
        'MenuElements',
        on_delete=models.CASCADE,
        verbose_name='Родительская категория',
        null=True,
        blank=True
    )
    abs_url = models.URLField('Абсолютный путь', max_length=255, null=True, blank=True)
    named_url = models.SlugField('Имя маршрута', max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        if self.abs_url:
            return self.abs_url
        return reverse(self.named_url)

    def clean(self):
        if not self.abs_url and not self.named_url:
            raise ValidationError('У пункта меню должен быть адрес')
        if self.named_url:
            try:
                reverse(self.named_url)
            except NoReverseMatch:
                raise ValidationError('Маршрута с таким именем не существует')
        if self.abs_url and not self.abs_url.endswith('/'):
            self.abs_url = self.abs_url + '/'

    def __str__(self):
        return self.name
