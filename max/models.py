from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from datetime import datetime

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=200, verbose_name='Категории')
    img = models.ImageField(upload_to='category', verbose_name='Фото', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('max:category', kwargs={'slug_category': self.slug})


class Edition(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = AutoSlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', editable=True)
    description = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to='max/static/max/edition', null=True, blank=True, verbose_name='Фото')
    pub_date = models.DateTimeField(default=datetime.now, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    relation = models.ForeignKey('Category', on_delete= models.CASCADE, null=True, verbose_name='Категории')
    
    class Meta:
        ordering = ['-slug']
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Books:library', kwargs={'slug_lib':self.slug})