from django.db import models
# from django.utils.safestring import  mark_safe
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField



class BlogCategory(models.Model):
    category = models.CharField('Название категории', max_length=300)
    slug = models.SlugField('URL-адрес', max_length=300)
    idSort = models.SmallIntegerField('Порядок сортировки', default=0)

    def get_absolute_url(self):
        return reverse('blog:group-blog', kwargs={'slug': self.slug})

    class Meta:
        ordering=['idSort']
        verbose_name = 'Разделы'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.category

class Posts(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, verbose_name='Категория')
    name = models.CharField('Название статьи', max_length=300)
    slug = models.SlugField('URL-адрес', max_length=300)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    edited = models.DateTimeField('Дата последнего редактирования', auto_now=True)
    text = RichTextUploadingField('Текст статьи')

    def get_absolute_url(self):
        return reverse('blog:postView', kwargs={'cut': self.category.slug, 'slug': self.slug})

    class Meta:
        ordering=['-created']
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статья'

    def __str__(self):
        return self.name