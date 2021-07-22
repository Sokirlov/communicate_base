from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutText(models.Model):
    title = models.CharField('Заголовок страницы', max_length=300)
    description = RichTextUploadingField('Текст на странице')

    class Meta:
        verbose_name = 'Про компанию'
        verbose_name_plural = 'Текст о компании'

    def __str__(self):
        return self.title