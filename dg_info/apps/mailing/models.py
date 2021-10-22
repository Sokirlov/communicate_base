from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from wokerlist.models import Staff, Group


class MailingModel(models.Model):
    daite_create = models.DateTimeField(auto_now_add=True)
    title_mail = models.CharField('Заголовок рассылки', max_length=300, default='From DG Info')
    file_mail = models.FileField('Добавленные файлы к рассылке', upload_to='', null=True, blank=True)
    text_mail = RichTextUploadingField()
    all_to_send = models.BooleanField('Разослать всем?', default=False)
    gorup_to_send = models.ManyToManyField(Group, blank=True)
    users_to_send = models.ManyToManyField(Staff, blank=True)
    start_send_email = models.BooleanField('Начать рассылку?', default=False)


    class Meta:
        verbose_name = 'Рассылку'
        verbose_name_plural = 'Рассылка по сотрудникам компании'

    def __str__(self):
        return self.title_mail
