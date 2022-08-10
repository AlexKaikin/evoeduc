from django.db import models
from django.urls import reverse
from pytils import translit


class Category(models.Model):
    """ Категории """
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    PUBLISHED = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, blank=True, unique=True, verbose_name="URL")
    published = models.CharField(choices=PUBLISHED, default='yes', max_length=3, verbose_name="Опубликована")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = translit.slugify(name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Post(models.Model):
    """ Статьи """
    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ('-created',)

    PUBLISHED = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    preview = models.TextField(verbose_name='Превью')
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=50, db_index=True, blank=True, unique=True, verbose_name="URL")
    published = models.CharField(choices=PUBLISHED, default='yes', max_length=3, verbose_name="Опубликована")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='posts', verbose_name='Категория')

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = translit.slugify(name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
