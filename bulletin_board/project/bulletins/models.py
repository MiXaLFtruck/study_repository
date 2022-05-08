from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from accounts.models import AppUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Category's name"))
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('incategory_list', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']


class Bulletin(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name=_('Author'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))
    slug = models.SlugField(max_length=128, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post_details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Bulletin')
        verbose_name_plural = _('Bulletins')
        ordering = ['title']


class Comment(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name=_('Author'))
    post = models.ForeignKey(Bulletin, on_delete=models.CASCADE, verbose_name=_('Post'))
    text = models.TextField(verbose_name=_('Text'))
    approved = models.BooleanField(verbose_name=_('Approved'), default=False)

    def __str__(self):
        return self.text[:64]

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
