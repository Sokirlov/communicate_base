from django.db import models

class HRDocs(models.Model):
    name = models.CharField('Название документа', max_length=500)
    date_create = models.DateTimeField(auto_now_add=True)
    filedoc = models.FileField(upload_to='documents/hr/', max_length=500)

    class Meta:
        ordering= ['-date_create']
        verbose_name= 'Кадровые документы'
        verbose_name_plural= 'Кадровые документы'

    def __str__(self):
        return self.name
