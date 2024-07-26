from django.db import models
from django.urls import reverse


class MenuList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MenuElements(models.Model):
    menu = models.ForeignKey(MenuList, on_delete=models.CASCADE, default=1)
    name = models.CharField('Название', max_length=20)
    parent = models.ForeignKey(
        'MenuElements',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    abs_url = models.URLField(max_length=255, null=True, blank=True)
    named_url = models.SlugField(max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        if self.abs_url:
            return self.abs_url
        return reverse(self.named_url)

    def __str__(self):
        return self.name
