from django.db import models
from django.urls import reverse

class ContractorsCategory(models.Model):
    category = models.CharField('Категория подрядных организаций', max_length=200)
    def get_absolute_url(self):
        return reverse('contractors:contractors_category', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Категория подрядчиков'
        verbose_name_plural = 'Категория подрядчиков'
    def __str__(self):
        return self.category




class Contractors(models.Model):
    last_edit = models.DateTimeField('Время последнего редактирования', auto_now=True)
    title = models.CharField('Название организации', max_length=500, unique=True)
    category = models.ForeignKey(ContractorsCategory, on_delete=models.PROTECT, verbose_name='Категория')
    tel = models.CharField('Номер телефона', max_length=20, null=True, blank=True)
    email = models.EmailField( verbose_name='e-mail', null=True, blank=True)
    adr = models.TextField('Адрес', max_length=1000, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('contractors:contractor_detail', kwargs={'category': self.category.id, 'pk': self.id})


    class Meta:
        ordering= ['last_edit']
        verbose_name= 'Подрядчики'
        verbose_name_plural= 'Подрядчики'
    def __str__(self):
        return self.title

class AditionalField(models.Model):
    name = models.CharField('Название поля', max_length=100)
    valuefield = models.CharField('Значение поля', max_length=500, null=True, blank=True)
    idSort = models.SmallIntegerField('Сортировка', default=0)
    contractors = models.ForeignKey(Contractors, on_delete=models.PROTECT)

    class Meta:
        ordering = ['idSort']
        verbose_name = 'Дополнительные поля'
        verbose_name_plural = 'Дополнительные поля'
    def __str__(self):
        return self.name